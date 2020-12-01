from SensorsActuators import Sensors
from SensorsActuators import Actuators

class UserSettings:
    def __init__(self):
        self.inlet_time = 5
        self.outlet_time = 5
        self.balance_time = 5
        self.max_pressure = 8
        self.min_pressure = 3
        self.process_pressure_min = 5 
        self.process_pressure_max = 8
        self.password = 0
        self.initialize = False
        self.initialRounds = 2
        self.last_purity=0

    def set_password(self,password):
        self.password = password

    def clamp(self,n, minn, maxn):
        if n < minn:
            return minn
        elif n > maxn:
            return maxn
        else:
            return n

    def set_inlet_time(self,time=32):
        '''
        Set time in sec for oxygen generator inlet stage.
        
            Parameters:
                    time : inlet time in sec.

            Returns:
                    none.
        '''
        self.clamp(time,6,60)
        self.inlet_time = time

    def get_inlet_time(self):
        '''
        Get time in sec for oxygen generator inlet stage.
        
            Parameters:
                    none.

            Returns:
                    inlet time in sec.
        '''
        return self.inlet_time
    
    def set_outlet_time(self,time=22):
        '''
        Set time in sec for oxygen generator outlet stage.
        
            Parameters:
                    time : outlet time in sec.

            Returns:
                    none.
        '''
        self.clamp(time,6,60)
        self.outlet_time = time

    def get_outlet_time(self):
        '''
        Get time in sec for oxygen generator outlet stage.
        
            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        return self.outlet_time
    
    def set_balance_time(self,time=14):
        '''
        Set time in sec for oxygen generator balance stage.
        
            Parameters:
                    time : balance time in sec.

            Returns:
                    none.
        '''
        self.clamp(time,6,60)
        self.balance_time = time

    def get_balance_time(self):
        '''
        Get time in sec for oxygen generator balance stage.
        
            Parameters:
                    none.

            Returns:
                    balance time in sec.
        '''
        return self.balance_time

    def set_max_pressure(self,pressure):
        '''
        Set the max limit for pressure.
        
            Parameters:
                    pressure : pressure value to set.

            Returns:
                    none.
        '''
        self.max_pressure = pressure

    def set_min_pressure(self,pressure):
        '''
        Set the min limit for pressure.
        
            Parameters:
                    pressure : pressure value to set.

            Returns:
                    none.
        '''
        self.min_pressure = pressure

    def test_sensor(self,sensor_name):
        '''
        Test the reading from a given sensor.
        
            Parameters:
                    sensor_check : Sensor to check.

            Returns:
                    reading of the sensor.
        '''
        if sensor_name == "press1":
            value = Sensors.sensors.read_pressure("press1")
        elif sensor_name == "press2":
            value = Sensors.sensors.read_pressure("press2")
        elif sensor_name == "press3":
            value = Sensors.sensors.read_pressure("press3")
        elif sensor_name == "press4":
            value = Sensors.sensors.read_pressure("press4")
        elif sensor_name == "press5":
            value = Sensors.sensors.read_pressure("press5")
        elif sensor_name == "oxy1":
            value = Sensors.sensors.read_pressure("oxy1")
        else:
            return False
        return value

    def test_valve_on(self,valve):
        '''
        Test the on state of a valve.
        
            Parameters:
                    valve : valve to turn on.

            Returns:
                    none.
        '''
        if valve == "left_in":
            print("Opening left_in")
            Actuators.valve.valve_open("left_in")
        elif valve == "right_in":
            print("Opening right_in")
            Actuators.valve.valve_open("right_in")
        elif valve == "balance_left":
            print("Opening balance_left")
            Actuators.valve.valve_open("balance_left")
        elif valve == "balance_right":
            print("Opening balance_right")
            Actuators.valve.valve_open("balance_right")
        elif valve == "left_out":
            print("Opening left_out")
            Actuators.valve.valve_open("left_out")
        elif valve == "right_out":
            print("Opening right_out")
            Actuators.valve.valve_open("right_out")
        else:
            return False
        return True
    
    def test_valve_off(self,valve):
        '''
        Turn off a valve after on test.
        
            Parameters:
                    valve : valve to turn off.

            Returns:
                    none.
        '''
        print("Turning all off.")
        Actuators.valve.valve_close_all()
        
user_settings = UserSettings()