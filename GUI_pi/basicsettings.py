# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\BasicSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI_pi.skeleton.basicsettingsSkeleton import Ui_Form

class BasicSettings(QtWidgets.QWidget, Ui_Form):
    switch_adv_settings = QtCore.pyqtSignal()
    switch_menu = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.advanced.clicked.connect(self.advsettingsbutton_handler)
        self.back.clicked.connect(self.backbutton_handler)

    def advsettingsbutton_handler(self):
        self.switch_adv_settings.emit()
    
    def backbutton_handler(self):
        self.switch_menu.emit()