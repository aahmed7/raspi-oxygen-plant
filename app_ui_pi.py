#!/usr/bin/python3

import sys
from PyQt5 import QtCore, QtWidgets
from GUI_pi import Login
from GUI_pi import mainwindow
from GUI_pi import basicsettings
from GUI_pi import AdvancedSettings
from GUI_pi import OutputTest
from GUI_pi import calibration
from GUI_pi import startstop
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import *
from SensorsActuators import Sensors
import os,time

class Controller:
    def __init__(self):
        self.login = Login.Login()
        self.main = mainwindow.MainWindow()
        self.basic_settings = basicsettings.BasicSettings()
        self.adv_settings = AdvancedSettings.AdvancedSettings()
        self.output_test_settings = OutputTest.OutputSettings()
        self.calibration_settings = calibration.Calibration()
        self.startstop = startstop.StartStop()
        self.thread = MainSensorThread()
        self.thread._signal.connect(self.signal_accept)
        self.thread.start()
        
    def hide_windows(self):
        self.adv_settings.close()
        self.basic_settings.close()
        self.login.close()
        self.main.close()
        self.output_test_settings.close()
        self.calibration_settings.close()

    def show_main(self):
        self.main.switch_settings.connect(self.show_basic_settings)
        self.main.dialog_startstop.connect(self.show_startstop)
        self.login.close()
        self.hide_windows()
        self.main.showFullScreen()

    def show_startstop(self):
        self.startstop.show()

    def show_basic_settings(self):
        self.basic_settings.switch_adv_settings.connect(self.show_login)
        self.basic_settings.switch_menu.connect(self.show_main)
        self.hide_windows()
        self.basic_settings.showFullScreen()

    def show_login(self):
        self.login.switch_window.connect(self.show_advanced_settings)
        self.login.show()
    
    def show_advanced_settings(self):
        self.adv_settings.switch_basic_settings.connect(self.show_basic_settings)
        self.adv_settings.switch_output_settings.connect(self.show_output_test_settings)
        self.adv_settings.switch_calibration_settings.connect(self.show_calibration_settings)
        self.hide_windows()
        self.adv_settings.showFullScreen()

    def show_output_test_settings(self):
        self.output_test_settings.switch_adv_settings.connect(self.show_advanced_settings)
        self.hide_windows()
        self.output_test_settings.showFullScreen()

    def show_calibration_settings(self):
        self.calibration_settings.switch_adv_settings.connect(self.show_advanced_settings)
        self.hide_windows()
        self.calibration_settings.showFullScreen()

    def signal_accept(self):
        self.main.airtank_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press3")))
        self.main.inlet_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press4")))
        self.main.left_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press1")))
        self.main.right_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press2")))
        self.main.oxy_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press5")))
        self.main.oxy_purity.setText("{:.1f}".format(Sensors.sensors.read_oxygen_sensor()))
        self.output_test_settings.airtank_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press3")))
        self.output_test_settings.inlet_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press4")))
        self.output_test_settings.left_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press1")))
        self.output_test_settings.right_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press2")))
        self.output_test_settings.oxy_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press5")))
        self.output_test_settings.oxy_purity.setText("{:.1f}".format(Sensors.sensors.read_oxygen_sensor()))
        

class MainSensorThread(QThread):
    _signal = pyqtSignal()

    @pyqtSlot()
    def run(self):
        while True:
            time.sleep(1)
            self._signal.emit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()