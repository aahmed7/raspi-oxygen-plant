from Settings import UserSettings
from SensorsActuators import Sensors
from SensorsActuators import Actuators
from time import time,sleep

# Oxygen generation is divided into 3 phases
# 1. inlet
# 2. balance
# 3. outlet
class Tanks:
    def check_inlet_safe_pressure(self,sensor_check):
        if Sensors.sensors.read_sensor(sensor_check) > 8:
            return False
        else:
            return True

    # This method will perform the first step of the Oxygen generator
    # process. inlet the oxygen to one of the two tanks.
    def inlet(self, mode="auto", selected_tank="left"):
        if selected_tank == "left":
            pressure_sensor = "press3"
            selected_valve = "left_in"
        else:
            pressure_sensor = "press4"
            selected_valve = "right_in"
        safety_check = self.check_inlet_safe_pressure(pressure_sensor)
        if safety_check == False:
            return False
        if mode=="manual":
            # Specify the running time for manual mode
            runtime = UserSettings.user_settings.get_time

            # Timeout after current time + running time
            timeout = time.time() + runtime

            while True:
                Actuators.valve.valve_open(selected_valve)

    def check_balance(self):
        return (Sensors.sensors.read_sensor("press3") - Sensors.sensors.read_sensor("press4"))

    # This is the second step. Balance the two tanks.
    def balance_tank(self):
        balance = self.check_balance()
        while abs(balance) < 0.05:
            if balance > 0:
                Actuators.valve.valve_close("balance_right")
                time.sleep(0.05)
                Actuators.valve.valve_open("balance_left")
            if balance < 0:
                Actuators.valve.valve_close("balance_left")
                time.sleep(0.05)
                Actuators.valve.valve_open("balance_right")
            
            time.sleep(0.2)
            balance = self.check_balance()
            
    def outlet(self,selected_tank="left"):
        if selected_tank == "left":
            pressure_sensor = "press3"
            selected_valve = "left_out"
        else:
            pressure_sensor = "press4"
            selected_valve = "right_out"

        # Specify the running time for manual mode
        runtime = UserSettings.user_settings.get_time

        # Timeout after current time + running time
        timeout = time.time() + runtime

        while True:
            Actuators.valve.valve_open(selected_valve)


    def fill_tank(self):
        pass

    def fill_left(self):
        pass

    def fill_right(self):
        pass