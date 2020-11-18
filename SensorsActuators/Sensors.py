import gpiozero
# Sensors are read using ADS1115
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import busio
import board

# Set GAIN to +/- 4.096V
GAIN = 1

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Define address for ADCs
ADC1 = 0x48
ADC2 = 0x49

# Create ADC objects
adc1 = ADS.ADS1115(i2c,address=ADC1)
adc2 = ADS.ADS1115(i2c,address=ADC2)

# Define index for sensors
PRESSURE1 = ADS.P0
PRESSURE2 = ADS.P1
PRESSURE3 = ADS.P2
PRESSURE4 = ADS.P0
PRESSURE5 = ADS.P1
OXYGEN1   = ADS.P2

class Sensors:
    # Initialize the ADC
    def __init__(self):
        self.press1 = AnalogIn(adc1,PRESSURE1)
        self.press2 = AnalogIn(adc1,PRESSURE2)
        self.press3 = AnalogIn(adc1,PRESSURE3)
        self.press4 = AnalogIn(adc2,PRESSURE4)
        self.press5 = AnalogIn(adc2,PRESSURE5)
        self.oxy1 = AnalogIn(adc2,OXYGEN1)

    def read_sensor(self, sensor_name="press1"):
        if sensor_name == "press1":
            return self.press1.value
        if sensor_name == "press2":
            return self.press2.value
        if sensor_name == "press3":
            return self.press3.value
        if sensor_name == "press4":
            return self.press4.value
        if sensor_name == "press5":
            return self.press5.value
        if sensor_name == "oxy1":
            return self.oxy1.value
        
sensors = Sensors()