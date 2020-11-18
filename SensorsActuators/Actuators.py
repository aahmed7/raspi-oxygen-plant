from gpiozero import DigitalOutputDevice

class Actuators:
    def __init__(self):
        self.left_in = DigitalOutputDevice(12)
        self.right_in = DigitalOutputDevice(16)
        self.balance_left = DigitalOutputDevice(18)
        self.balance_right = DigitalOutputDevice(22)
        self.left_out = DigitalOutputDevice(24)
        self.right_out = DigitalOutputDevice(32)

    def valve_open(self, valve):
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
        self.left_in.off()
        self.right_in.off()
        self.balance_left.off()
        self.balance_right.off()
        self.left_out.off()
        self.right_out.off()

valve = Actuators()