# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\startstop.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.skeleton.StartStopSkeleton import Ui_Dialog

class StartStop(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

        # self.back.clicked.connect()
