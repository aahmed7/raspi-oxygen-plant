import gpiozero
# Sensors are read using ADS1115
import Adafruit_ADS1x15.ads1115 as ADS
from Adafruit_ADS1x15.analog_in import AnalogIn
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
adc1 = ADS.ADS1115(i2c, address=ADC1)
adc2 = ADS.ADS1115(i2c, address=ADC2)

# Define index for sensors
PRESSURE1 = ADS.P0
PRESSURE2 = ADS.P1
PRESSURE3 = ADS.P2
PRESSURE4 = ADS.P0
PRESSURE5 = ADS.P1
OXYGEN1 = ADS.P2


class Sensors:
    """This class contains methods for directly interacting with the sensors.

    Attributes:
        press1 : airtank pressure sensor object
        press2 : inlet pressure sensor object
        press3 : left tank pressure sensor object
        press4 : right tank pressure sensor object
        press5 : oxygen tank pressure sensor object
        oxy1 : oxygen purity sensor object
    """

    def __init__(self):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        self.press1 = AnalogIn(adc1, PRESSURE1)
        self.press2 = AnalogIn(adc1, PRESSURE2)
        self.press3 = AnalogIn(adc1, PRESSURE3)
        self.press4 = AnalogIn(adc2, PRESSURE4)
        self.press5 = AnalogIn(adc2, PRESSURE5)
        self.oxy1 = AnalogIn(adc2, OXYGEN1)
        # Resistor installed on the board for volt -> current conversion
        self.RES = 200
        # Scale current to pressure. scaler = 20mA/PRESSURE_SENSOR_MAX
        self.PRESSURE_SCALER = 1
        # Scale current to oxygen. scaler = 20mA/OXYGEN_SENSOR_MAX
        self.OXY_SCALER = 1

    def set_pressure_sensor_range(self, pressure_sensor_max):
        '''
        Set pressure sensor range

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        self.PRESSURE_SCALER = .02/pressure_sensor_max

    def set_oxygen_sensor_range(self, oxygen_sensor_max):
        '''
        Get time in sec for oxygen generator outlet stage.

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        self.OXY_SCALER = .02/oxygen_sensor_max

    def read_sensor(self, sensor_name="press1"):
        '''
        Raw read a sensor

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        if sensor_name == "press1":
            return (self.press1.value)
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

    def read_pressure(self, sensor_name="press1"):
        '''
        Read pressure from a sensor. Set the pressure sensor range manually

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        if sensor_name == "press1":
            return (self.press1.value/32768.0)*5.0/self.RES*1000*self.PRESSURE_SCALER
        if sensor_name == "press2":
            return self.press2.value/32768.0*5.0/self.RES*1000*self.PRESSURE_SCALER
        if sensor_name == "press3":
            return self.press3.value/32768.0*5.0/self.RES*1000*self.PRESSURE_SCALER
        if sensor_name == "press4":
            return self.press4.value/32768.0*5.0/self.RES*1000*self.PRESSURE_SCALER
        if sensor_name == "press5":
            return self.press5.value/32768.0*5.0/self.RES*1000*self.PRESSURE_SCALER

    def read_oxygen_sensor(self):
        '''
        Get the oxygen %age purity

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        return (self.oxy1.value/32768.0)*5.0/self.RES*1000*self.OXY_SCALER


sensors = Sensors()
