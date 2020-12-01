from Settings import UserSettings
from SensorsActuators import Sensors
from SensorsActuators import Actuators
import time

# Oxygen generation is divided into 3 phases
# 1. inlet
# 2. balance
# 3. outlet
class Tanks:
    def check_inlet_safe_pressure(self,sensor_check):
        '''
        Checks if a given pressure sensor is in safe range

            Parameters:
                    sensor_check : Sensor to check.

            Returns:
                    boolean indicating safe state.
        '''
        sensor_value = Sensors.sensors.read_pressure(sensor_check)
        print("Pressure_"+sensor_check+"="+str(sensor_value))
        if sensor_check == "press1" or sensor_check == "press2":
            if sensor_value > UserSettings.user_settings.max_pressure or sensor_value < UserSettings.user_settings.min_pressure:
                return False
            else:
                return True
        elif sensor_check == "press3" or sensor_check == "press4" or sensor_check == "press5":
            if sensor_value > UserSettings.user_settings.process_pressure_max:
                return False
            else:
                return True
        else:
            print("Invalid Sensor.")
            return False

    def watch_pressure_sensors(self):
        '''
        watch the inlet and airtank pressure sensors.
        
            Parameters:
                    none.

            Returns:
                    boolean indicating safe state.
        '''
        sensor_value = Sensors.sensors.read_pressure("press1")
        if sensor_value > UserSettings.user_settings.max_pressure or sensor_value < UserSettings.user_settings.min_pressure:
            print("Press1 exceeded. Stopping.")
            return False

        sensor_value = Sensors.sensors.read_pressure("press1")
        if sensor_value > UserSettings.user_settings.max_pressure or sensor_value < UserSettings.user_settings.min_pressure:
            print("Press2 exceeded. Stopping.")
            return False
        return True

    def watch_pressure_sensors_for_time(self,runtime):
        '''
        watch the inlet and airtank pressure sensors for a
        given time.
        
            Parameters:
                    runtime : time to check continuously check
                    the sensors.

            Returns:
                    boolean indicating safe state.
        '''
        start_time = time.time()
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time > (runtime/2):
                break
            time.sleep(1)
            if self.watch_pressure_sensors() == False:
                return False

    def inlet(self, selected_tank="left"):
        '''
        This method will perform the first step of the Oxygen generator
        process. inlet the oxygen to one of the two tanks.
        
            Parameters:
                    selected_tank : Sensor to check.

            Returns:
                    boolean indicating process success or interruption.
        '''
        print("Starting inlet stage for "+selected_tank+" tank")
        if selected_tank == "left":
            pressure_sensor = "press3"
            selected_valve = "left_in"
        else:
            pressure_sensor = "press4"
            selected_valve = "right_in"
        safety_check = self.check_inlet_safe_pressure(pressure_sensor)
        # Inlet will be skipped if the pressure is already in required range.
        if safety_check == False:
            print("Pressure out of range. Skipping.")
            return False
        # Get the running time.
        runtime = UserSettings.user_settings.get_inlet_time()

        # Open valve, and don't close. this will stay open till stage 2.
        Actuators.valve.valve_open(selected_valve)
        if self.watch_pressure_sensors_for_time(runtime)==False:
            return False
        return True

    def balance_tank(self,selected_tank="left"):
        '''
        This is the final step. Balance the two tanks.
        
            Parameters:
                    selected_tank : Sensor to check.

            Returns:
                    boolean indicating process success or interruption.
        '''
        print("Starting balance stage for "+selected_tank+" tank")
        if selected_tank == "left":
            primary_balance = "balance_left"
            secondary_balance = "balance_right"
        else:
            primary_balance = "balance_right"
            secondary_balance = "balance_left"

        # Get the running time.
        runtime = UserSettings.user_settings.get_balance_time()

        if self.watch_pressure_sensors() == False:
            return False
        Actuators.valve.valve_open(primary_balance)
       
        # Turn on secondary balance after half time.
        start_time = time.time()
        if self.watch_pressure_sensors_for_time(runtime)==False:
            return False
        Actuators.valve.valve_open(secondary_balance)
        
        start_time = time.time()
        if self.watch_pressure_sensors_for_time(runtime)==False:
            return False
        Actuators.valve.valve_close_all()
        return True

    def outlet(self,selected_tank="left"):
        '''
        This is the second step. Open the outlet valve.
        
            Parameters:
                    selected_tank : Sensor to check.

            Returns:
                    boolean indicating process success or interruption.
        '''
        print("Starting outlet stage for "+selected_tank+" tank")
        if selected_tank == "left":
            selected_valve_in = "left_int"
            selected_valve_out = "left_out"
            selected_valve_balance = "balance_left"
        else:
            selected_valve_in = "right_int"
            selected_valve_out = "right_out"
            selected_valve_balance = "balance_right"

        # Specify the running time for manual mode.
        runtime = UserSettings.user_settings.get_outlet_time()

        if self.watch_pressure_sensors() == False:
            return False
        # Open in and out valves.
        Actuators.valve.valve_open(selected_valve_in)
        Actuators.valve.valve_open(selected_valve_out)
        Actuators.valve.valve_open(selected_valve_balance)
        # Close balance After 1 sec.
        time.sleep(1)
        Actuators.valve.valve_close(selected_valve_balance)
        if self.watch_pressure_sensors() == False:
            return False
        # Open balance again for 1 sec after half time.
        # Close balance After 1 sec.
        if self.watch_pressure_sensors_for_time(runtime)==False:
            return False
        Actuators.valve.valve_open(selected_valve_balance)
        time.sleep(1)
        Actuators.valve.valve_close(selected_valve_balance)
        if self.watch_pressure_sensors() == False:
            return False
        if self.watch_pressure_sensors_for_time(runtime)==False:
            return False
        Actuators.valve.valve_close_all()
        return True

    def fill_tank(self,initialize=False,mode="manual",tank="default"):
        '''
        This method runs one cycle of the algorithm.
        
            Args:
                    initialize: initializing stage? This stage skips inlet.
                    mode: manual or auto mode.
                    tank: left or right tank.

            Returns:
                    boolean indicating process success or interruption.
        '''
        try:
            if tank == "default":
                print("No tank selected")
                return False

            # Set the purity value if initializing
            if initialize == True:
                self.last_purity= Sensors.sensors.read_oxygen_sensor()

            # Check if Air tank pressure is in range.
            if self.check_inlet_safe_pressure("press1")==False:
                print("Inlet at press1 not in range")
                return False
            
            # Check if Oxygen Generator inlet is in range.
            if self.check_inlet_safe_pressure("press2")==False:
                print("Inlet at press2 not in range")
                return False

            # Step 1, skip if not in range or if initializing.
            if initialize == True:
                if self.inlet(tank) == False:
                    Actuators.valve.valve_close_all()
                    return False

            # Step 2, outlet.
            if self.outlet(tank) == False:
                Actuators.valve.valve_close_all()
                return False

            # Step 3, balance.
            if self.balance_tank(tank) == False:
                Actuators.valve.valve_close_all()
                return False

            # If mode is auto, then update the time for all stages
            if mode=="auto" and initialize != True:
                current_purity = Sensors.sensors.read_oxygen_sensor() - self.last_purity
                if current_purity > 0:
                    UserSettings.user_settings.set_inlet_time(UserSettings.user_settings.get_inlet_time()+6)
                    UserSettings.user_settings.set_outlet_time(UserSettings.user_settings.get_outlet_time()+6)
                    UserSettings.user_settings.set_balance_time(UserSettings.user_settings.get_balance_time()+6)
                elif current_purity < 0:
                    UserSettings.user_settings.set_inlet_time(UserSettings.user_settings.get_inlet_time()-6)
                    UserSettings.user_settings.set_outlet_time(UserSettings.user_settings.get_outlet_time()-6)
                    UserSettings.user_settings.set_balance_time(UserSettings.user_settings.get_balance_time()-6)
                self.last_purity= Sensors.sensors.read_oxygen_sensor()

            return True
        except:
            print("An Error Occured.")
            Actuators.valve.valve_close_all()
            return False

tanks = Tanks()