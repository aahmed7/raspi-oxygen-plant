class UserSettings:
    def __init__(self):
        self.time = 20

    # Set time in sec for oxygen generator operations
    def set_time(self,time):
        self.time = time

    # Get time in sec for oxygen generator operations
    def get_time(self):
        return self.time

    # Function prototype
    def adjust_pressure(self,tank_index):
        pass

    # Function prototype
    def set_filling_time(self,tank_index):
        pass

    # Function prototype
    def test_valve(self,):
        pass

user_settings = UserSettings()