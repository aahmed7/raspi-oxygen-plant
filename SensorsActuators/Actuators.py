from gpiozero import DigitalOutputDevice

class Actuators:
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
        self.alarm = DigitalOutputDevice("BOARD7")
        self.left_in = DigitalOutputDevice("BOARD12")
        self.right_in = DigitalOutputDevice("BOARD16")
        self.balance_left = DigitalOutputDevice("BOARD18")
        self.balance_right = DigitalOutputDevice("BOARD22")
        self.left_out = DigitalOutputDevice("BOARD24")
        self.right_out = DigitalOutputDevice("BOARD32")

    def valve_open(self, valve):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        print("Opening "+valve)
        if valve == "left_in":
            self.left_in.on()
        if valve == "right_in":
            self.right_in.on()
        if valve == "balance_left":
            self.balance_left.on()
        if valve == "balance_right":
            self.balance_right.on()
        if valve == "left_out":
            self.left_out.on()
        if valve == "right_out":
            self.right_out.on()

    def valve_close(self,valve):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        print("Closing "+valve)
        if valve == "left_in":
            self.left_in.off()
        if valve == "right_in":
            self.right_in.off()
        if valve == "balance_left":
            self.balance_left.off()
        if valve == "balance_right":
            self.balance_right.off()
        if valve == "left_out":
            self.left_out.off()
        if valve == "right_out":
            self.right_out.off()

    def valve_close_all(self):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        print("Closing All Valves.")
        self.left_in.off()
        self.right_in.off()
        self.balance_left.off()
        self.balance_right.off()
        self.left_out.off()
        self.right_out.off()

    def alarm_on(self):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        self.alarm.on()

    def alarm_off(self):
        '''
        Initialize the ADC

            Parameters:
                    none.

            Returns:
                    outlet time in sec.
        '''
        self.alarm.off()

valve = Actuators()