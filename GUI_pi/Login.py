from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from Settings import UserSettings

class Login(QtWidgets.QWidget):
	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		super().__init__()
		self.setWindowTitle('Login Form')
		self.resize(500, 120)

		layout = QGridLayout()

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)

		button_login = QPushButton('Login')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		self.setLayout(layout)

	def check_password(self):
		msg = QMessageBox()

		if self.lineEdit_password.text() == str(UserSettings.user_settings.password):
			self.switch_window.emit()
		else:
			msg.setText('Incorrect Password')
			msg.exec_()