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
adc1 = ADS.ADS1115(ADC1,i2c)
adc2 = ADS.ADS1115(ADC2,i2c)

# Define index for sensors
PRESSURE1 = ADS.P0
PRESSURE2 = ADS.P1
PRESSURE3 = ADS.P2
PRESSURE4 = ADS.P0
PRESSURE5 = ADS.P1
OXYGEN1   = ADS.P2

press1 = AnalogIn(adc1,PRESSURE1)
press2 = AnalogIn(adc1,PRESSURE2)
press3 = AnalogIn(adc1,PRESSURE3)
press4 = AnalogIn(adc2,PRESSURE4)
press5 = AnalogIn(adc2,PRESSURE5)
oxy1 = AnalogIn(adc2,OXYGEN1)

class Sensors:
    # Initialize the ADC
    def __init__(self):
        pass

    def read_sensor(self, sensor_name):
        if sensor_name == "press1":
            return press1.value
        
