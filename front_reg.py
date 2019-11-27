# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fsoci\Desktop\databaseFiles\reg_window.ui',
# licensing of 'C:\Users\fsoci\Desktop\databaseFiles\reg_window.ui' applies.
#
# Created: Wed Nov 27 23:04:37 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_reg_window(object):
    def setupUi(self, reg_window):
        reg_window.setObjectName("reg_window")
        reg_window.resize(240, 181)
        self.line_log = QtWidgets.QLineEdit(reg_window)
        self.line_log.setGeometry(QtCore.QRect(10, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.line_log.setFont(font)
        self.line_log.setObjectName("line_log")
        self.line_pass = QtWidgets.QLineEdit(reg_window)
        self.line_pass.setGeometry(QtCore.QRect(10, 50, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.line_pass.setFont(font)
        self.line_pass.setObjectName("line_pass")
        self.line_repeat_pass = QtWidgets.QLineEdit(reg_window)
        self.line_repeat_pass.setGeometry(QtCore.QRect(10, 90, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.line_repeat_pass.setFont(font)
        self.line_repeat_pass.setObjectName("line_repeat_pass")
        self.button_register = QtWidgets.QPushButton(reg_window)
        self.button_register.setGeometry(QtCore.QRect(10, 130, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.button_register.setFont(font)
        self.button_register.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_register.setObjectName("button_register")

        self.retranslateUi(reg_window)
        QtCore.QMetaObject.connectSlotsByName(reg_window)

    def retranslateUi(self, reg_window):
        reg_window.setWindowTitle(QtWidgets.QApplication.translate("reg_window", "Form", None, -1))
        self.line_log.setPlaceholderText(QtWidgets.QApplication.translate("reg_window", "login", None, -1))
        self.line_pass.setPlaceholderText(QtWidgets.QApplication.translate("reg_window", "password", None, -1))
        self.line_repeat_pass.setPlaceholderText(QtWidgets.QApplication.translate("reg_window", "repeat pass", None, -1))
        self.button_register.setText(QtWidgets.QApplication.translate("reg_window", "REGISTER", None, -1))

