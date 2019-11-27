# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fsoci\Desktop\databaseFiles\message_window.ui',
# licensing of 'C:\Users\fsoci\Desktop\databaseFiles\message_window.ui' applies.
#
# Created: Wed Nov 27 23:04:37 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_message_window(object):
    def setupUi(self, message_window):
        message_window.setObjectName("message_window")
        message_window.resize(506, 286)
        message_window.setMinimumSize(QtCore.QSize(506, 236))
        message_window.setMaximumSize(QtCore.QSize(506, 286))
        self.line_title = QtWidgets.QLineEdit(message_window)
        self.line_title.setGeometry(QtCore.QRect(10, 10, 491, 31))
        self.line_title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.line_title.setFont(font)
        self.line_title.setAutoFillBackground(False)
        self.line_title.setClearButtonEnabled(True)
        self.line_title.setObjectName("line_title")
        self.window_text = QtWidgets.QTextEdit(message_window)
        self.window_text.setGeometry(QtCore.QRect(10, 50, 491, 181))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.window_text.setFont(font)
        self.window_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.window_text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window_text.setOverwriteMode(False)
        self.window_text.setObjectName("window_text")
        self.button_confirm = QtWidgets.QPushButton(message_window)
        self.button_confirm.setGeometry(QtCore.QRect(10, 240, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.button_confirm.setFont(font)
        self.button_confirm.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_confirm.setObjectName("button_confirm")

        self.retranslateUi(message_window)
        QtCore.QMetaObject.connectSlotsByName(message_window)

    def retranslateUi(self, message_window):
        message_window.setWindowTitle(QtWidgets.QApplication.translate("message_window", "Form", None, -1))
        self.line_title.setPlaceholderText(QtWidgets.QApplication.translate("message_window", "title", None, -1))
        self.window_text.setPlaceholderText(QtWidgets.QApplication.translate("message_window", "text", None, -1))
        self.button_confirm.setText(QtWidgets.QApplication.translate("message_window", "Confirm", None, -1))

