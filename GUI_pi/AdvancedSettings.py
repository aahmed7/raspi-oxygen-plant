# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AdvancedSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from GUI_pi.skeleton.AdvancedSettingsSkeleton import Ui_Form
from Settings import UserSettings

class AdvancedSettings(QtWidgets.QWidget, Ui_Form):

    switch_basic_settings = QtCore.pyqtSignal()
    switch_output_settings = QtCore.pyqtSignal()
    switch_calibration_settings = QtCore.pyqtSignal()
    update_passwd = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.back.clicked.connect(self.basicsettingsbutton_handler)
        self.Output_test.clicked.connect(self.switch_output_settings)
        self.Calibration.clicked.connect(self.switch_calibration_settings)
        self.inlet_time.setValue(UserSettings.user_settings.inlet_time)
        self.outlet_time.setValue(UserSettings.user_settings.outlet_time)
        self.balance_wait.setValue(UserSettings.user_settings.balance_time)
        self.initial_press.setValue(UserSettings.user_settings.min_pressure)
        self.final_press.setValue(UserSettings.user_settings.max_pressure)
        self.update_pass.clicked.connect(self.update_password)

        self.factory_reset.clicked.connect(self.factory_reset_func)
        self.password.setPlainText(str(UserSettings.user_settings.password))

    def basicsettingsbutton_handler(self):
        self.switch_basic_settings.emit()

    def outputsettingsbutton_handler(self):
        self.switch_output_settings.emit()

    def calibrationsettingsbutton_handler(self):
        self.switch_calibration_settings.emit()

    def factory_reset_func(self):
        UserSettings.user_settings.set_inlet_time()
        UserSettings.user_settings.set_outlet_time()
        UserSettings.user_settings.set_balance_time()
        UserSettings.user_settings.set_min_pressure(3)
        UserSettings.user_settings.set_max_pressure(8)
        self.inlet_time.setValue(UserSettings.user_settings.inlet_time)
        self.outlet_time.setValue(UserSettings.user_settings.outlet_time)
        self.balance_wait.setValue(UserSettings.user_settings.balance_time)
        self.initial_press.setValue(UserSettings.user_settings.min_pressure)
        self.final_press.setValue(UserSettings.user_settings.max_pressure)
        # self.password.setValue(UserSettings.user_settings.password)
        self.inlet_time.valueChanged.connect(self.update_inlet_time)
        self.outlet_time.valueChanged.connect(self.update_outlet_time)
        self.balance_wait.valueChanged.connect(self.update_balance_time)
        self.initial_press.valueChanged.connect(self.update_min_pressure)
        self.final_press.valueChanged.connect(self.update_max_pressure)
        self.update_pass.clicked.connect(self.update_password)

        self.init_btn.clicked.connect(self.initializer_update)

    def update_inlet_time(self):
        UserSettings.user_settings.set_inlet_time(int(self.inlet_time.value()))
    def update_outlet_time(self):
        UserSettings.user_settings.set_outlet_time(int(self.outlet_time.value()))
    def update_balance_time(self):
        UserSettings.user_settings.set_balance_time(int(self.balance_wait.value()))
    def update_min_pressure(self):
        UserSettings.user_settings.set_min_pressure(int(self.initial_press.value()))
    def update_max_pressure(self):
        UserSettings.user_settings.set_max_pressure(int(self.final_press.value()))
    def update_password(self):
        self.update_passwd.emit()

    def initializer_update(self):
        UserSettings.user_settings.initialize = True
        UserSettings.user_settings.initialRounds = self.initial_rounds.value()