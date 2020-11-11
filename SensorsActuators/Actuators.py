from gpiozero import PWMOutputDevice

led = PWMOutputDevice(4)

class Actuators:
    def __init__(self):
        print("object created.")

    def set_duty(self,duty=0):
        global led
        led.value = duty

    def power_on(self):
        global led
        led.on()

    def power_off(self):
        global led
        led.off()
