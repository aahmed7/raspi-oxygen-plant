# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\startstop.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtWidgets,QtGui,QtCore
from GUI_pi.skeleton.StartStopSkeleton import Ui_Dialog
from PyQt5.QtCore import *

class StartStop(QtWidgets.QDialog, Ui_Dialog):
    start_process = QtCore.pyqtSignal()
    stop_process = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

        self.icon_on = QtGui.QIcon()
        self.icon_on.addPixmap(QtGui.QPixmap(":/img/on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_off = QtGui.QIcon()
        self.icon_off.addPixmap(QtGui.QPixmap(":/img/off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.back.clicked.connect(self.back_btn_handler)
        self.startstop.clicked.connect(self.startstop_handler)
        self.auto_btn.clicked.connect(self.autobtn_handler)

        self.process = False
        self.auto = False

    def back_btn_handler(self):
        self.auto_btn.setEnabled(True)
        self.stop_process.emit()
        self.startstop.setIcon(self.icon_off)
        self.startstop.setIconSize(QtCore.QSize(100, 200))
        self.close()
        
    def startstop_handler(self):
        if self.process == False:
            self.process = True
            self.startstop.setIcon(self.icon_on)
            self.startstop.setIconSize(QtCore.QSize(100, 200))
            self.start_process.emit()
            self.auto_btn.setEnabled(False)
        else:
            self.process = False
            self.stop_process.emit()
            self.startstop.setIcon(self.icon_off)
            self.startstop.setIconSize(QtCore.QSize(100, 200))
            self.auto_btn.setEnabled(True)

    def hardstop(self):
        self.process = False
        self.startstop.setIcon(self.icon_off)
        self.startstop.setIconSize(QtCore.QSize(100, 200))
        self.auto_btn.setEnabled(True)

    def autobtn_handler(self):
        if self.auto == True:
            self.auto = False
            self.auto_btn.setIcon(self.icon_off)
            self.auto_btn.setIconSize(QtCore.QSize(100, 200))
        else:
            self.auto = True
            self.auto_btn.setIcon(self.icon_on)
            self.auto_btn.setIconSize(QtCore.QSize(100, 200))
