# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fsoci\Desktop\databaseFiles\database_.ui',
# licensing of 'C:\Users\fsoci\Desktop\databaseFiles\database_.ui' applies.
#
# Created: Wed Nov 27 23:04:37 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_NoteList(object):
    def setupUi(self, NoteList):
        NoteList.setObjectName("NoteList")
        NoteList.resize(900, 700)
        NoteList.setMinimumSize(QtCore.QSize(560, 700))
        NoteList.setMaximumSize(QtCore.QSize(900, 700))
        NoteList.setStyleSheet("background-coor: rgb(214, 214, 214)")
        self.centralwidget = QtWidgets.QWidget(NoteList)
        self.centralwidget.setObjectName("centralwidget")
        self.line_login = QtWidgets.QLineEdit(self.centralwidget)
        self.line_login.setGeometry(QtCore.QRect(10, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.line_login.setFont(font)
        self.line_login.setStatusTip("")
        self.line_login.setPlaceholderText("login")
        self.line_login.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.line_login.setClearButtonEnabled(True)
        self.line_login.setObjectName("line_login")
        self.line_password = QtWidgets.QLineEdit(self.centralwidget)
        self.line_password.setGeometry(QtCore.QRect(10, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.line_password.setFont(font)
        self.line_password.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.line_password.setClearButtonEnabled(True)
        self.line_password.setObjectName("line_password")
        self.button_log = QtWidgets.QPushButton(self.centralwidget)
        self.button_log.setGeometry(QtCore.QRect(220, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.button_log.setFont(font)
        self.button_log.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_log.setObjectName("button_log")
        self.button_sign = QtWidgets.QPushButton(self.centralwidget)
        self.button_sign.setGeometry(QtCore.QRect(220, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.button_sign.setFont(font)
        self.button_sign.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_sign.setObjectName("button_sign")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(420, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.button_add.setFont(font)
        self.button_add.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_add.setObjectName("button_add")
        self.button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete.setGeometry(QtCore.QRect(560, 10, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.button_delete.setFont(font)
        self.button_delete.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_delete.setObjectName("button_delete")
        self.button_edit = QtWidgets.QPushButton(self.centralwidget)
        self.button_edit.setGeometry(QtCore.QRect(770, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.button_edit.setFont(font)
        self.button_edit.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_edit.setObjectName("button_edit")
        self.table_w = QtWidgets.QTableWidget(self.centralwidget)
        self.table_w.setGeometry(QtCore.QRect(10, 90, 881, 581))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.table_w.setFont(font)
        self.table_w.setStatusTip("")
        self.table_w.setAutoFillBackground(False)
        self.table_w.setObjectName("table_w")
        self.table_w.setColumnCount(3)
        self.table_w.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_w.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_w.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_w.setHorizontalHeaderItem(2, item)
        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(420, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.button_send.setFont(font)
        self.button_send.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_send.setObjectName("button_send")
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(770, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.button_save.setFont(font)
        self.button_save.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_save.setObjectName("button_save")
        NoteList.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NoteList)
        self.statusbar.setObjectName("statusbar")
        NoteList.setStatusBar(self.statusbar)

        self.retranslateUi(NoteList)
        QtCore.QMetaObject.connectSlotsByName(NoteList)

    def retranslateUi(self, NoteList):
        NoteList.setWindowTitle(QtWidgets.QApplication.translate("NoteList", "MainWindow", None, -1))
        self.line_password.setPlaceholderText(QtWidgets.QApplication.translate("NoteList", "password", None, -1))
        self.button_log.setText(QtWidgets.QApplication.translate("NoteList", "LOG IN", None, -1))
        self.button_sign.setText(QtWidgets.QApplication.translate("NoteList", "SIGN UP", None, -1))
        self.button_add.setText(QtWidgets.QApplication.translate("NoteList", "ADD", None, -1))
        self.button_delete.setText(QtWidgets.QApplication.translate("NoteList", "DELETE", None, -1))
        self.button_edit.setText(QtWidgets.QApplication.translate("NoteList", "EDIT", None, -1))
        self.table_w.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("NoteList", "Date", None, -1))
        self.table_w.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("NoteList", "Title", None, -1))
        self.table_w.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("NoteList", "Text", None, -1))
        self.button_send.setText(QtWidgets.QApplication.translate("NoteList", "SEND", None, -1))
        self.button_save.setText(QtWidgets.QApplication.translate("NoteList", "SAVE", None, -1))

