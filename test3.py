import Tanks,time
from Settings import UserSettings
from SensorsActuators import Actuators

if __name__ == "__main__":
    UserSettings.user_settings.set_time(5)
    if Tanks.tanks.fill_tank("manual","left") == True:
        print("Process Complete")
    else:
        Actuators.valve.alarm_on()
        print("Unable to complete process")
        time.sleep(3)
        Actuators.valve.alarm_off()