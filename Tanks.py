from Settings import UserSettings
from SensorsActuators import Sensors
from SensorsActuators import Actuators
import time, threading

# Oxygen generation is divided into 3 phases
# 1. inlet
# 2. balance
# 3. outlet
class Tanks:
    def check_inlet_safe_pressure(self,sensor_check):
        sensor_value = Sensors.sensors.read_pressure(sensor_check)
        print("Pressure_"+sensor_check+"="+str(sensor_value))
        if sensor_check == "press1" or sensor_check == "press2":
            if sensor_value > 8 or sensor_value < 5:
                return False
            else:
                return True
        elif sensor_check == "press3" or sensor_check == "press4" or sensor_check == "press5":
            if sensor_value > 8:
                return False
            else:
                return True
        else:
            print("Invalid Sensor.")
            return False

    def watch_pressure_sensors(self):
        sensor_value = Sensors.sensors.read_pressure("press1")
        if sensor_value > 8 or sensor_value < 5:
            print("Press1 exceeded. Stopping.")
            return False

        sensor_value = Sensors.sensors.read_pressure("press1")
        if sensor_value > 8 or sensor_value < 5:
            print("Press2 exceeded. Stopping.")
            return False
        return True
            
    # This method will perform the first step of the Oxygen generator
    # process. inlet the oxygen to one of the two tanks.
    def inlet(self, selected_tank="left"):
        print("Starting inlet stage for "+selected_tank+" tank")
        if selected_tank == "left":
            pressure_sensor = "press3"
            selected_valve = "left_in"
        else:
            pressure_sensor = "press4"
            selected_valve = "right_in"
        safety_check = self.check_inlet_safe_pressure(pressure_sensor)
        if safety_check == False:
            print("Pressure out of range. Skipping.")
            return False
        # Get the running time
        runtime = UserSettings.user_settings.get_time()

        # Open valve, and don't close. this will stay open till stage 2
        Actuators.valve.valve_open(selected_valve)
        for i in range(runtime-1):
            time.sleep(i)
            if self.watch_pressure_sensors() == False:
                return False
        return True

    # This is the second step. Balance the two tanks.
    def balance_tank(self,selected_tank="left"):
        print("Starting balance stage for "+selected_tank+" tank")
        if selected_tank == "left":
            primary_balance = "balance_left"
            secondary_balance = "balance_right"
        else:
            primary_balance = "balance_right"
            secondary_balance = "balance_left"

        # Get the running time
        runtime = UserSettings.user_settings.get_time()

        if self.watch_pressure_sensors() == False:
            return False

        Actuators.valve.valve_open(primary_balance)
        # Turn on secondary balance after half time
        for i in range(int(runtime/2)):
            time.sleep(i)
            if self.watch_pressure_sensors() == False:
                return False
        Actuators.valve.valve_open(secondary_balance)
        
        for i in range(int(runtime/2)):
            time.sleep(i)
            if self.watch_pressure_sensors() == False:
                return False
        Actuators.valve.valve_close_all()
        return True

    def outlet(self,selected_tank="left"):
        print("Starting outlet stage for "+selected_tank+" tank")
        if selected_tank == "left":
            selected_valve_in = "left_int"
            selected_valve_out = "left_out"
            selected_valve_balance = "balance_left"
        else:
            selected_valve_in = "right_int"
            selected_valve_out = "right_out"
            selected_valve_balance = "balance_right"

        # Specify the running time for manual mode
        runtime = UserSettings.user_settings.get_time()

        if self.watch_pressure_sensors() == False:
            return False
        # Open in and out valves
        Actuators.valve.valve_open(selected_valve_in)
        Actuators.valve.valve_open(selected_valve_out)
        Actuators.valve.valve_open(selected_valve_balance)
        # Close balance After 1 sec
        time.sleep(1)
        Actuators.valve.valve_close(selected_valve_balance)
        if self.watch_pressure_sensors() == False:
            return False
        # Open balance again for 1 sec after half time
        # Close balance After 1 sec
        for i in range(int(runtime/2)):
            time.sleep(i)
            if self.watch_pressure_sensors() == False:
                return False
        Actuators.valve.valve_open(selected_valve_balance)
        time.sleep(1)
        Actuators.valve.valve_close(selected_valve_balance)
        if self.watch_pressure_sensors() == False:
            return False
        for i in range(int(runtime/2)):
            time.sleep(i)
            if self.watch_pressure_sensors() == False:
                return False
        Actuators.valve.valve_close_all()
        return True

    def fill_tank(self,mode="manual",tank="default"):
        try:
            if tank == "default":
                print("No tank selected")
                return False

            # Check if Air tank pressure is in range
            if self.check_inlet_safe_pressure("press1")==False:
                print("Inlet at press1 not in range")
                return False
            
            # Check if Oxygent Generator inlet is in range
            if self.check_inlet_safe_pressure("press2")==False:
                print("Inlet at press2 not in range")
                return False

            # Step 1, skip if not in range.
            if self.inlet(tank) == False:
                Actuators.valve.valve_close_all()
                return False

            # Step 2, outlet
            if self.outlet(tank) == False:
                Actuators.valve.valve_close_all()
                return False

            # Step 3, balance
            if self.balance_tank(tank) == False:
                Actuators.valve.valve_close_all()
                return False

            return True
        except:
            print("An Error Occured.")
            Actuators.valve.valve_close_all()
            return False

tanks = Tanks()