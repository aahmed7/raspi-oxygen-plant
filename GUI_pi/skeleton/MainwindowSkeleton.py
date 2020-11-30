# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\CODING_LAB\PY_QT\test1\test1\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 480)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 501, 480))
        self.widget.setStyleSheet("color: rgb(220, 220, 220);")
        self.widget.setObjectName("widget")
        self.left_tank = QtWidgets.QProgressBar(self.widget)
        self.left_tank.setGeometry(QtCore.QRect(96, 140, 91, 201))
        self.left_tank.setProperty("value", 24)
        self.left_tank.setTextVisible(False)
        self.left_tank.setOrientation(QtCore.Qt.Vertical)
        self.left_tank.setObjectName("left_tank")
        self.v3 = QtWidgets.QLabel(self.widget)
        self.v3.setGeometry(QtCore.QRect(170, 390, 40, 21))
        self.v3.setText("")
        self.v3.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        self.v3.setScaledContents(True)
        self.v3.setObjectName("v3")
        self.right_tank = QtWidgets.QProgressBar(self.widget)
        self.right_tank.setGeometry(QtCore.QRect(276, 140, 91, 201))
        self.right_tank.setProperty("value", 24)
        self.right_tank.setTextVisible(False)
        self.right_tank.setOrientation(QtCore.Qt.Vertical)
        self.right_tank.setObjectName("right_tank")
        self.tankview = QtWidgets.QLabel(self.widget)
        self.tankview.setGeometry(QtCore.QRect(0, 20, 451, 441))
        self.tankview.setStyleSheet("")
        self.tankview.setText("")
        self.tankview.setPixmap(QtGui.QPixmap(":/img/tankview.png"))
        self.tankview.setScaledContents(True)
        self.tankview.setObjectName("tankview")
        self.v4 = QtWidgets.QLabel(self.widget)
        self.v4.setGeometry(QtCore.QRect(260, 390, 40, 21))
        self.v4.setText("")
        self.v4.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        self.v4.setScaledContents(True)
        self.v4.setObjectName("v4")
        self.left_press = QtWidgets.QLabel(self.widget)
        self.left_press.setGeometry(QtCore.QRect(30, 228, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.left_press.setFont(font)
        self.left_press.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: none;")
        self.left_press.setObjectName("left_press")
        self.oxy_press = QtWidgets.QLabel(self.widget)
        self.oxy_press.setGeometry(QtCore.QRect(400, 120, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.oxy_press.setFont(font)
        self.oxy_press.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: none;")
        self.oxy_press.setObjectName("oxy_press")
        self.airtank_press = QtWidgets.QLabel(self.widget)
        self.airtank_press.setGeometry(QtCore.QRect(36, 392, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.airtank_press.setFont(font)
        self.airtank_press.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: none;")
        self.airtank_press.setObjectName("airtank_press")
        self.inlet_press = QtWidgets.QLabel(self.widget)
        self.inlet_press.setGeometry(QtCore.QRect(376, 408, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.inlet_press.setFont(font)
        self.inlet_press.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: none;")
        self.inlet_press.setObjectName("inlet_press")
        self.oxy_purity = QtWidgets.QLabel(self.widget)
        self.oxy_purity.setGeometry(QtCore.QRect(380, 44, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.oxy_purity.setFont(font)
        self.oxy_purity.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: none;")
        self.oxy_purity.setObjectName("oxy_purity")
        self.right_press = QtWidgets.QLabel(self.widget)
        self.right_press.setGeometry(QtCore.QRect(404, 232, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.right_press.setFont(font)
        self.right_press.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: none;")
        self.right_press.setObjectName("right_press")
        self.rightin_valve = QtWidgets.QLabel(self.widget)
        self.rightin_valve.setGeometry(QtCore.QRect(260, 420, 40, 20))
        self.rightin_valve.setText("")
        self.rightin_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        self.rightin_valve.setScaledContents(True)
        self.rightin_valve.setObjectName("rightin_valve")
        self.bright_valve = QtWidgets.QLabel(self.widget)
        self.bright_valve.setGeometry(QtCore.QRect(210, 88, 40, 20))
        self.bright_valve.setText("")
        self.bright_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        self.bright_valve.setScaledContents(True)
        self.bright_valve.setObjectName("bright_valve")
        self.leftout_valve = QtWidgets.QLabel(self.widget)
        self.leftout_valve.setGeometry(QtCore.QRect(162, 43, 40, 21))
        self.leftout_valve.setText("")
        self.leftout_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        self.leftout_valve.setScaledContents(True)
        self.leftout_valve.setObjectName("leftout_valve")
        self.rightout_valve = QtWidgets.QLabel(self.widget)
        self.rightout_valve.setGeometry(QtCore.QRect(262, 43, 40, 21))
        self.rightout_valve.setText("")
        self.rightout_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        self.rightout_valve.setScaledContents(True)
        self.rightout_valve.setObjectName("rightout_valve")
        self.leftin_valve = QtWidgets.QLabel(self.widget)
        self.leftin_valve.setGeometry(QtCore.QRect(170, 420, 40, 21))
        self.leftin_valve.setText("")
        self.leftin_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        self.leftin_valve.setScaledContents(True)
        self.leftin_valve.setObjectName("leftin_valve")
        self.bleft_valve = QtWidgets.QLabel(self.widget)
        self.bleft_valve.setGeometry(QtCore.QRect(212, 64, 40, 20))
        self.bleft_valve.setText("")
        self.bleft_valve.setPixmap(QtGui.QPixmap(":/img/valve_close.png"))
        self.bleft_valve.setScaledContents(True)
        self.bleft_valve.setObjectName("bleft_valve")
        self.tankview.raise_()
        self.left_tank.raise_()
        self.v3.raise_()
        self.right_tank.raise_()
        self.v4.raise_()
        self.left_press.raise_()
        self.oxy_press.raise_()
        self.airtank_press.raise_()
        self.inlet_press.raise_()
        self.oxy_purity.raise_()
        self.right_press.raise_()
        self.rightin_valve.raise_()
        self.bright_valve.raise_()
        self.leftout_valve.raise_()
        self.rightout_valve.raise_()
        self.leftin_valve.raise_()
        self.bleft_valve.raise_()
        self.LOGO = QtWidgets.QLabel(Form)
        self.LOGO.setGeometry(QtCore.QRect(500, 0, 351, 101))
        self.LOGO.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LOGO.setText("")
        self.LOGO.setObjectName("LOGO")
        self.TITLE = QtWidgets.QLabel(Form)
        self.TITLE.setGeometry(QtCore.QRect(500, 100, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TITLE.setFont(font)
        self.TITLE.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(43, 225, 43);")
        self.TITLE.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE.setObjectName("TITLE")
        self.BG = QtWidgets.QLabel(Form)
        self.BG.setGeometry(QtCore.QRect(500, 430, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BG.setFont(font)
        self.BG.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.BG.setText("")
        self.BG.setAlignment(QtCore.Qt.AlignCenter)
        self.BG.setObjectName("BG")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(500, 430, 301, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 184, 89);")
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.settings_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.settings_btn.setFont(font)
        self.settings_btn.setStyleSheet("background-color: rgb(66, 255, 72);\n"
"color: rgb(255, 255, 255);")
        self.settings_btn.setObjectName("settings_btn")
        self.horizontalLayout.addWidget(self.settings_btn)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(500, 170, 291, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.status_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("background-color: rgb(231, 147, 52);\n"
"color: rgb(255, 255, 255);")
        self.status_label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.status_label.setLineWidth(0)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)
        self.status_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.status_text.setFont(font)
        self.status_text.setStyleSheet("background-color: rgb(64, 66, 188);\n"
"color: rgb(255, 255, 255);")
        self.status_text.setLineWidth(0)
        self.status_text.setAlignment(QtCore.Qt.AlignCenter)
        self.status_text.setObjectName("status_text")
        self.verticalLayout.addWidget(self.status_text)
        self.Runtime_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Runtime_label.setFont(font)
        self.Runtime_label.setStyleSheet("background-color: rgb(231, 147, 52);\n"
"color: rgb(255, 255, 255);")
        self.Runtime_label.setLineWidth(0)
        self.Runtime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Runtime_label.setObjectName("Runtime_label")
        self.verticalLayout.addWidget(self.Runtime_label)
        self.Runtime_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Runtime_text.setFont(font)
        self.Runtime_text.setStyleSheet("background-color: rgb(64, 66, 188);\n"
"color: rgb(255, 255, 255);")
        self.Runtime_text.setLineWidth(0)
        self.Runtime_text.setAlignment(QtCore.Qt.AlignCenter)
        self.Runtime_text.setObjectName("Runtime_text")
        self.verticalLayout.addWidget(self.Runtime_text)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.LOGO.raise_()
        self.widget.raise_()
        self.TITLE.raise_()
        self.BG.raise_()
        self.horizontalLayoutWidget.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.left_press.setText(_translate("Form", "1.0"))
        self.oxy_press.setText(_translate("Form", "1.0"))
        self.airtank_press.setText(_translate("Form", "1.0"))
        self.inlet_press.setText(_translate("Form", "1.0"))
        self.oxy_purity.setText(_translate("Form", "1.0"))
        self.right_press.setText(_translate("Form", "1.0"))
        self.TITLE.setText(_translate("Form", "Home"))
        self.start.setText(_translate("Form", "Start"))
        self.settings_btn.setText(_translate("Form", "Settings"))
        self.status_label.setText(_translate("Form", "Status"))
        self.status_text.setText(_translate("Form", "Off"))
        self.Runtime_label.setText(_translate("Form", "Run time for Stage"))
        self.Runtime_text.setText(_translate("Form", "0.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
import tankresources_rc