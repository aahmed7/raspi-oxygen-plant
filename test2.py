# from SensorsActuators import Sensors
from SensorsActuators import Actuators
import time

print("Opening left_in")
Actuators.valve.valve_open("left_in")
time.sleep(0.5)

print("Opening right_in")
Actuators.valve.valve_open("right_in")
time.sleep(0.5)

print("Opening balance_left")
Actuators.valve.valve_open("balance_left")
time.sleep(0.5)

print("Opening balance_right")
Actuators.valve.valve_open("balance_right")
time.sleep(0.5)

print("Opening left_out")
Actuators.valve.valve_open("left_out")
time.sleep(0.5)

print("Opening right_out")
Actuators.valve.valve_open("right_out")
time.sleep(0.5)

print("Turning all off.")
Actuators.valve.valve_close_all()