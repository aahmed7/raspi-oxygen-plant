#!/usr/bin/python3

from Settings import UserSettings
import sys
from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
# from GUI_pi import Login
from GUI_pi import mainwindow
from GUI_pi import basicsettings
from GUI_pi import AdvancedSettings
from GUI_pi import OutputTest
from GUI_pi import calibration
from GUI_pi import startstop
from GUI_pi import LoginKeypad
from GUI_pi import setpasswdkeypad
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import *
from SensorsActuators import Sensors
from SensorsActuators import Actuators
from datetime import datetime
import Tanks
import os,time

class Controller:
    def __init__(self):
        self.login = LoginKeypad.Keypad()
        self.main = mainwindow.MainWindow()
        self.basic_settings = basicsettings.BasicSettings()
        self.adv_settings = AdvancedSettings.AdvancedSettings()
        self.output_test_settings = OutputTest.OutputSettings()
        self.calibration_settings = calibration.Calibration()
        self.startstop = startstop.StartStop()
        self.updatepass = setpasswdkeypad.SetPasswd()
        self.sensorupdatethread = MainSensorThread()
        self.sensorupdatethread._signal.connect(self.update_sensor_gauges)
        self.sensorupdatethread.start()
        self.processctrlthread = ProcessControlThread()
        self.processctrlthread._statusUpdateSignal.connect(self.update_status_text)
        self.processctrlthread._runtimeUpdateSignal.connect(self.update_time_text)
        self.processctrlthread._valveopenUISignal.connect(self.update_valveopen_ui)
        self.processctrlthread._valvecloseUISignal.connect(self.update_valveclose_ui)
        self.processctrlthread._initializeComplete.connect(self.startstop.hardstop)
        
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
        self.startstop.start_process.connect(self.start_process_handler)
        self.startstop.stop_process.connect(self.stop_process_handler)

    def show_basic_settings(self):
        self.basic_settings.switch_adv_settings.connect(self.show_login)
        self.basic_settings.switch_menu.connect(self.show_main)
        self.hide_windows()
        self.basic_settings.showFullScreen()

    def show_login(self):
        self.login.unlock_settings.connect(self.show_advanced_settings)
        self.login.show()
    
    def show_advanced_settings(self):
        self.adv_settings.switch_basic_settings.connect(self.show_basic_settings)
        self.adv_settings.switch_output_settings.connect(self.show_output_test_settings)
        self.adv_settings.switch_calibration_settings.connect(self.show_calibration_settings)
        self.adv_settings.update_passwd.connect(self.show_passwdupdate_keypad)
        self.hide_windows()
        self.adv_settings.showFullScreen()

    def show_passwdupdate_keypad(self):
        self.updatepass.updated.connect(self.updatePasswd)
        self.updatepass.show()

    def updatePasswd(self):
        self.adv_settings.password.setPlainText(str(UserSettings.user_settings.password))

    def show_output_test_settings(self):
        self.output_test_settings.switch_adv_settings.connect(self.show_advanced_settings)
        self.hide_windows()
        self.output_test_settings.showFullScreen()

    def show_calibration_settings(self):
        self.calibration_settings.switch_adv_settings.connect(self.show_advanced_settings)
        self.hide_windows()
        self.calibration_settings.showFullScreen()

    def update_sensor_gauges(self):
        self.main.airtank_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press1")))
        self.main.inlet_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press2")))
        self.main.left_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press3")))
        self.main.right_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press4")))
        self.main.oxy_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press5")))
        self.main.oxy_purity.setText("{:.1f}".format(Sensors.sensors.read_oxygen_sensor()))
        self.output_test_settings.airtank_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press3")))
        self.output_test_settings.inlet_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press4")))
        self.output_test_settings.left_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press1")))
        self.output_test_settings.right_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press2")))
        self.output_test_settings.oxy_press.setText("{:.1f}".format(Sensors.sensors.read_pressure("press5")))
        self.output_test_settings.oxy_purity.setText("{:.1f}".format(Sensors.sensors.read_oxygen_sensor()))
        self.main.left_tank.setMaximum(20/Sensors.sensors.PRESSURE_SCALER3)
        self.main.left_tank.setValue(Sensors.sensors.read_pressure("press3"))
        self.main.right_tank.setMaximum(20/Sensors.sensors.PRESSURE_SCALER4)
        self.main.right_tank.setValue(Sensors.sensors.read_pressure("press4"))
        now = datetime.now()
        self.basic_settings.date.setText(now.strftime("%d/%m/%Y"))
        self.basic_settings.time.setText(now.strftime("%H:%M:%S"))

    def start_process_handler(self):
        UserSettings.user_settings.last_purity=Sensors.sensors.read_oxygen_sensor()
        msg = QMessageBox()
        Actuators.valve.valve_close_all()
        self.main.status_text.setText("Starting")
        if not self.processctrlthread.isRunning():
            self.processctrlthread.start()
            msg.setText('Process started.')
            # msg.exec_()

    def stop_process_handler(self):
        msg = QMessageBox()
        self.main.status_text.setText("Off")
        self.main.Runtime_text.setText("Off")
        self.update_valvecloseall_ui()
        Actuators.valve.valve_close_all()
        if self.processctrlthread.isRunning():
            self.processctrlthread.stop()
            msg.setText('Process Will stop when current stage is complete.')
            msg.exec_()

    def process_main(self):
        pass

    def update_status_text(self,msg):
        self.main.status_text.setText(msg)

    def update_time_text(self,msg):
        self.main.Runtime_text.setText(msg)

    def update_valveopen_ui(self,msg):
        if msg == "leftin":
            self.main.leftin_valve.setPixmap(QtGui.QPixmap(":/img/valve_open.png"))
        if msg == "rightin":
            self.main.rightin_valve.setPixmap(QtGui.QPixmap(":/img/valve_open.png"))
        if msg == "bleft":
            self.main.bleft_valve.setPixmap(QtGui.QPixmap(":/img/valve_open.png"))
        if msg == "bright":
            self.main.bright_valve.setPixmap(QtGui.QPixmap(":/img/valve_open.png"))
        if msg == "leftout":
            self.main.leftout_valve.setPixmap(QtGui.QPixmap(":/img/valve_open.png"))
        if msg == "rightout":
            self.main.rightout_valve.setPixmap(QtGui.QPixmap(":/img/valve_open.png"))

    def update_valveclose_ui(self,msg):
        if msg == "leftin":
            self.main.leftin_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        if msg == "rightin":
            self.main.rightin_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        if msg == "bleft":
            self.main.bleft_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        if msg == "bright":
            self.main.bright_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        if msg == "leftout":
            self.main.leftout_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        if msg == "rightout":
            self.main.rightout_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))

    def update_valvecloseall_ui(self):
        self.update_valveclose_ui("leftin")
        self.update_valveclose_ui("rightin")
        self.update_valveclose_ui("bleft")
        self.update_valveclose_ui("bright")
        self.update_valveclose_ui("leftout")
        self.update_valveclose_ui("rightout")

class MainSensorThread(QThread):
    _signal = pyqtSignal()

    @pyqtSlot()
    def run(self):
        while True:
            time.sleep(1)
            self._signal.emit()

class ProcessControlThread(QThread):
    _statusUpdateSignal = pyqtSignal(str)
    _runtimeUpdateSignal = pyqtSignal(str)
    _valveopenUISignal = pyqtSignal(str)
    _valvecloseUISignal = pyqtSignal(str)
    _initializeComplete = pyqtSignal()
    stage = ["inlet", "outlet","balance"]
    tank = ["left","right"]

    def __init__(self, parent=None):
        super(ProcessControlThread, self).__init__(parent)
        self._stopped = True

    def __del__(self):
        self.wait()

    @pyqtSlot()
    def run(self):
        msg = QMessageBox()
        self._stopped = False
        i=0
        j=0
        if UserSettings.user_settings.initialize == True:
            rounds=0
            while rounds < UserSettings.user_settings.initialRounds:
                print("process running.")
                if self.stage[i] == "inlet" and self.tank[j]=="left":
                    # Check if Air tank pressure is in range.
                    if Tanks.tanks.check_inlet_safe_pressure("press1")==False:
                        msg.setText("Airtank Pressure not in range")
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    # Check if Oxygen Generator inlet is in range.
                    if Tanks.tanks.check_inlet_safe_pressure("press2")==False:
                        msg.setText('Inlet pressure not in range')
                        self._initializeComplete.emit()
                        msg.exec_()
                        return                                           #<===  
                    self._valveopenUISignal.emit("leftin")
                    self._runtimeUpdateSignal.emit(str(UserSettings.user_settings.inlet_time))
                    self._statusUpdateSignal.emit("Intial Left Inlet")
                    if Tanks.tanks.inlet("left") == False:
                        msg.setText('Presure limit exceeded')
                        msg.exec_()
                        return
                    self._valvecloseUISignal.emit("leftin")

                if self.stage[i] == "balance" and self.tank[j]=="left":
                    self._valveopenUISignal.emit("bleft")
                    # time.sleep(1)                                            #<===
                    self._statusUpdateSignal.emit("Intial Left Balance")
                    self._runtimeUpdateSignal.emit(str(UserSettings.user_settings.balance_time))
                    if Tanks.tanks.balance_tank("left") == False:
                        msg.setText('Presure limit exceeded.')
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    self._valvecloseUISignal.emit("bleft")

                if self.stage[i] == "inlet" and self.tank[j]=="right":
                    # Check if Air tank pressure is in range.
                    if Tanks.tanks.check_inlet_safe_pressure("press1")==False:
                        msg.setText("Airtank Pressure not in range")
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    # Check if Oxygen Generator inlet is in range.
                    if Tanks.tanks.check_inlet_safe_pressure("press2")==False:
                        msg.setText("Inlet Pressure not in range")
                        self._initializeComplete.emit()
                        msg.exec_()
                        return 
                    self._valveopenUISignal.emit("rightin")
                    time.sleep(1)                                            #<=== 
                    self._statusUpdateSignal.emit("Intial Right Inlet")
                    self._runtimeUpdateSignal.emit(str(UserSettings.user_settings.inlet_time))
                    if Tanks.tanks.inlet("right") == False:
                        msg.setText('Presure limit exceeded')
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    self._valvecloseUISignal.emit("rightin")

                if self.stage[i] == "balance" and self.tank[j]=="right":
                    self._valveopenUISignal.emit("bright")
                    time.sleep(1)                                            #<=== 
                    self._statusUpdateSignal.emit("Intial Right Balance")
                    self._runtimeUpdateSignal.emit(str(UserSettings.user_settings.balance_time))
                    if Tanks.tanks.balance_tank("right") == False:
                        msg.setText('Presure limit exceeded')
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    self._valvecloseUISignal.emit("bright")

                i+=1
                if i>2:
                    i=0
                    j+=1
                if j>1:
                    j=0
                    rounds+=1
                if self._stopped:
                    return
            # Set initialize to false after initialization
            UserSettings.user_settings.initialize = False
            Actuators.valve.valve_close_all()
            self._initializeComplete.emit()
            msg = QMessageBox()
            msg.setText('Initialization Complete. To re-run initialization, press initialize in advanced settings')
            msg.exec_()

        else:
            while True:
                print("process running.")
                if self.stage[i] == "inlet" and self.tank[j]=="left":
                    # Check if Air tank pressure is in range.
                    if Tanks.tanks.check_inlet_safe_pressure("press1")==False:
                        msg.setText("Airtank Pressure not in range")
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    # Check if Oxygen Generator inlet is in range.
                    if Tanks.tanks.check_inlet_safe_pressure("press2")==False:
                        msg.setText("Inlet Pressure not in range")
                        self._initializeComplete.emit()
                        msg.exec_()
                        return 
                    self._valveopenUISignal.emit("leftin")
                    self._statusUpdateSignal.emit("Left Inlet")
                    self._runtimeUpdateSignal.emit(str(UserSettings.user_settings.inlet_time))
                    if Tanks.tanks.inlet("left") == False:
                        msg.setText('Presure limit exceeded.')
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    # time.sleep(1)                                            #<===  
                    self._valvecloseUISignal.emit("leftin")

                if self.stage[i] == "outlet" and self.tank[j]=="left":
                    self._valveopenUISignal.emit("leftout")
                    # time.sleep(1)                                            #<=== 
                    self._statusUpdateSignal.emit("Left Outlet")
                    self._runtimeUpdateSignal.emit(str(UserSettings.user_settings.outlet_time))
                    if Tanks.tanks.outlet("left") == False:
                        msg.setText('Presure limit exceeded.')
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    self._valvecloseUISignal.emit("leftout")

                if self.stage[i] == "balance" and self.tank[j]=="left":
                    self._valveopenUISignal.emit("bleft")
                    # time.sleep(1)                                            #<=== 
                    self._statusUpdateSignal.emit("Left Balance")
                    self._runtimeUpdateSignal.emit(str(UserSettings.user_settings.balance_time))
                    if Tanks.tanks.balance_tank("left") == False:
                        msg.setText('Presure limit exceeded.')
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    self._valvecloseUISignal.emit("bleft")

                if self.stage[i] == "inlet" and self.tank[j]=="right":
                    # Check if Air tank pressure is in range.
                    if Tanks.tanks.check_inlet_safe_pressure("press1")==False:
                        msg.setText("Airtank Pressure not in range")
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    # Check if Oxygen Generator inlet is in range.
                    if Tanks.tanks.check_inlet_safe_pressure("press2")==False:
                        msg.setText("Inlet Pressure not in range")
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    self._valveopenUISignal.emit("rightin")
                    # time.sleep(1)                                            #<===  
                    self._statusUpdateSignal.emit("Right Inlet")
                    self._runtimeUpdateSignal.emit(str(UserSettings.user_settings.inlet_time))
                    if Tanks.tanks.inlet("right") == False:
                        msg.setText('Presure limit exceeded.')
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    self._valvecloseUISignal.emit("rightin")

                if self.stage[i] == "outlet" and self.tank[j]=="right":
                    self._valveopenUISignal.emit("rightout")
                    # time.sleep(1)                                            #<=== 
                    self._statusUpdateSignal.emit("Right Outlet")
                    self._runtimeUpdateSignal.emit(str(UserSettings.user_settings.outlet_time))
                    if Tanks.tanks.outlet("right") == False:
                        msg.setText('Presure limit exceeded.')
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    self._valvecloseUISignal.emit("rightout")

                if self.stage[i] == "balance" and self.tank[j]=="right":
                    self._valveopenUISignal.emit("bright")
                    self._statusUpdateSignal.emit("Right Balance")
                    self._runtimeUpdateSignal.emit(str(UserSettings.user_settings.balance_time))
                    if Tanks.tanks.balance_tank("right") == False:
                        msg.setText('Presure limit exceeded.')
                        self._initializeComplete.emit()
                        msg.exec_()
                        return
                    # time.sleep(1)                                            #<=== 
                    self._valvecloseUISignal.emit("bright")

                i+=1
                if i>2:
                    i=0
                    j+=1
                if j>1:
                    j=0
                if self._stopped:
                    return

    def stop(self):
        Actuators.valve.valve_close_all()
        self._stopped = True

# QApplication caller code. Write all code above this line.
def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        main()
    except:
        main()