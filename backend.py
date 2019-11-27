from sqlite3.dbapi2 import Cursor
from typing import TextIO

from frontend import *
from front_reg import Ui_reg_window
from message_window import Ui_message_window
from PySide2.QtWidgets import QMessageBox

import sqlite3

import datetime
import sys
import ast

try:
    with open('users.txt', 'x') as file:
        file.write('[]')
except FileExistsError:
    pass


class MessageWindow(QtWidgets.QWidget, Ui_message_window):

    def __init__(self, parent=None):
        super(MessageWindow, self).__init__(parent)
        self.setupUi(self)

        self.parent = parent
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint)

        self.button_confirm.clicked.connect(self.buttonConfirm)

    def buttonConfirm(self):
        self.parent.title = self.line_title.text()
        self.parent.text = self.window_text.toPlainText()
        self.hide()


class RegWindow(QtWidgets.QWidget, Ui_reg_window):

    def __init__(self, parent=None):
        super(RegWindow, self).__init__(parent)
        self.setupUi(self)

        self.parent = parent
        self.setWindowFlags(QtCore.Qt.Window)  # | QtCore.Qt.WindowStaysOnTopHint)

        self.line_log.setMaxLength(13)
        self.line_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass.setMaxLength(13)
        self.line_repeat_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_repeat_pass.setMaxLength(13)

        self.button_register.clicked.connect(self.buttonRegister)

    def buttonRegister(self):  # CHECK IF LOGIN/PASSWORD ALREADY IN DB
        self.login = self.line_log.text()
        self.password = self.line_pass.text()
        if self.password == self.line_repeat_pass.text() and self.password != '':
            this_file: TextIO
            with open('users.txt', 'r+') as this_file:
                data = ast.literal_eval(this_file.read())
                if self.login not in [i['login'] for i in data]:

                    self.parent.login = self.login
                    self.parent.password = self.password
                    self.parent.line_login.setText(self.login)
                    self.parent.line_password.setText(self.password)

                    data.append({'login': self.login, 'password': self.password})
                    this_file.seek(0)
                    this_file.write(str(data))
                    message = QtWidgets.QMessageBox()
                    message.setWindowTitle('Success')
                    message.setText('Registration successful')
                    message.setIcon(message.Information)
                    message.exec()
                    self.hide()
                else:
                    message = QtWidgets.QMessageBox()
                    message.setWindowTitle('Bad')
                    message.setText('User with such login already exists')
                    message.setIcon(message.Warning)
                    message.exec()

        else:
            message = QtWidgets.QMessageBox()
            message.setWindowTitle('Error')
            message.setText('Passwords doesn\'t match')
            message.setIcon(message.Warning)
            message.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)
            message.exec()


class Main(QtWidgets.QMainWindow, Ui_NoteList):

    title: bool

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        # создание бд если ее нет
        connection = sqlite3.connect('base.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS dataBaseTable (person_id TEXT, c_date TEXT, title TEXT, text TEXT)')
        cursor.close()
        connection.close()

        # колличество столбцов и расшириние последнего
        self.table_w.setColumnCount(3)
        self.table_w.horizontalHeader().setStretchLastSection(True)

        # Запоминание для удаления строки
        self.table_w.cellClicked[int, int].connect(self.clickedRowColumn)
        self.table_w.cellActivated[int, int].connect(self.activatedRowColumn)

        # Установка ширины столбца
        self.table_w.setColumnWidth(0, 220)
        self.table_w.setColumnWidth(1, 160)

        # Это свойство содержит политику переноса текста в элементе
        self.table_w.setWordWrap(False)

        self.table_w.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # цвета и размер ячеек
        self.table_w.verticalHeader().setDefaultSectionSize(33)
        self.table_w.setAlternatingRowColors(True)

        self.list_of_extended_rows = []

        # политика скрытия пароля
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setMaxLength(13)

        self.title, self.text, self.login = False, False, False

        # связка нажатия клавиш и функций
        self.button_log.clicked.connect(self.buttonLog)
        self.button_sign.clicked.connect(self.buttonReg)
        self.button_add.clicked.connect(self.buttonAdd)
        self.button_edit.clicked.connect(self.buttonEdit)
        self.button_send.clicked.connect(self.buttonSend)
        self.button_delete.clicked.connect(self.buttonDelete)
        self.button_save.clicked.connect(self.buttonSave)

    def buttonLog(self):
        self.login = self.line_login.text()
        self.password = self.line_password.text()

        # открытие файла для дальнейшей сверки логина\пароля с базой и выписка данных в таблицу
        this_file: TextIO
        with open('users.txt', 'r') as this_file:
            data = ast.literal_eval(this_file.read())
            if self.login in [i['login'] for i in data] and self.password in [i['password'] for i in data]:
                connection = sqlite3.connect('base.db')
                cursor: Cursor = connection.cursor()
                cursor.execute('SELECT * FROM dataBaseTable WHERE person_id=(?)', (self.login,))
                fetch, count = cursor.fetchall(), 0
                self.table_w.setRowCount(len(fetch) + 1)
                for p_id, date_time, title, text in fetch:
                    self.table_w.setItem(count, 0, QtWidgets.QTableWidgetItem(date_time))
                    self.table_w.setItem(count, 1, QtWidgets.QTableWidgetItem(title))
                    self.table_w.setItem(count, 2, QtWidgets.QTableWidgetItem(text))
                    count += 1
                cursor.close()
                connection.close()

                message = QtWidgets.QMessageBox()
                message.setWindowTitle('Success')
                message.setText('Log In successful')
                message.setIcon(message.Information)
                message.exec()
            else:
                message = QtWidgets.QMessageBox()
                message.setWindowTitle('Bad')
                message.setText('Wrong login or password!')
                message.setIcon(message.Warning)
                message.exec()

    def buttonReg(self):
        self.window = RegWindow(self)
        self.window.show()

    def buttonEdit(self):
        if self.login:
            self.win: MessageWindow = MessageWindow(self)
            self.win.show()
        else:
            pass

    def buttonAdd(self):
        if self.login:
            self.win: MessageWindow = MessageWindow(self)
            self.win.show()
        else:
            pass

    def buttonDelete(self):
        # удаление эллементов и перезаполнение таблицы
        try:
            connection = sqlite3.connect('base.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM dataBaseTable WHERE person_id = (?)', (self.login,))
            fetch = cursor.fetchall()

            cursor.execute('DELETE FROM dataBaseTable WHERE person_id = (?) and c_date = (?) and title = (?)',
                           (self.login, fetch[self.row][1], fetch[self.row][2]))
            connection.commit()
            self.table_w.setRowCount(0)
            self.table_w.setRowCount(len(fetch))

            cursor.execute('SELECT * FROM dataBaseTable WHERE person_id = (?)', (self.login,))
            fetch, count = cursor.fetchall(), 0
            for p_id, date_time, title, text in fetch:
                self.table_w.setItem(count, 0, QtWidgets.QTableWidgetItem(date_time))
                self.table_w.setItem(count, 1, QtWidgets.QTableWidgetItem(title))
                self.table_w.setItem(count, 2, QtWidgets.QTableWidgetItem(text))
                count += 1

            cursor.close()
            connection.close()
        except AttributeError:
            pass

    def buttonSave(self):
        try:
            connection = sqlite3.connect('base.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM dataBaseTable WHERE person_id = (?)', (self.login,))
            fetch = cursor.fetchall()

            cursor.execute('UPDATE dataBaseTable SET title = (?), text = (?) WHERE person_id = (?) and c_date = (?)'
                           'and title = (?)', (self.title, self.text, self.login, fetch[self.row][1], fetch[self.row][2]))
            connection.commit()

            if self.login:
                self.table_w.setRowCount(0)
                self.table_w.setRowCount(len(fetch) + 1)

                cursor.execute('SELECT * FROM dataBaseTable WHERE person_id = (?)', (self.login,))
                fetch, count = cursor.fetchall(), 0
                for p_id, date_time, title, text in fetch:
                    self.table_w.setItem(count, 0, QtWidgets.QTableWidgetItem(date_time))
                    self.table_w.setItem(count, 1, QtWidgets.QTableWidgetItem(title))
                    self.table_w.setItem(count, 2, QtWidgets.QTableWidgetItem(text))
                    count += 1
            else:
                pass

            cursor.close()
            connection.close()
        except AttributeError:
            pass

    def buttonSend(self):

        # добавляем запись в бд
        time = str(datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S'))
        title = self.title
        text = self.text

        connection = sqlite3.connect('base.db')
        cursor = connection.cursor()
        if self.title and self.text:
            cursor.execute('INSERT INTO dataBaseTable (person_id, c_date, title, text) VALUES (?, ?, ?, ?)',
                           (self.login, time, title, text))
            connection.commit()
        else:
            pass
        cursor.execute('SELECT * FROM dataBaseTable WHERE person_id=(?)', (self.login,))
        fetch, count = cursor.fetchall(), 0
        for p_id, date_time, title, text in fetch:
            self.table_w.setItem(count, 0, QtWidgets.QTableWidgetItem(date_time))
            self.table_w.setItem(count, 1, QtWidgets.QTableWidgetItem(title))
            self.table_w.setItem(count, 2, QtWidgets.QTableWidgetItem(text))
            count += 1

        if self.login:
            self.table_w.setRowCount(len(fetch) + 1)
        else:
            pass

        self.title, self.text = False, False

        cursor.close()
        connection.close()

    def clickedRowColumn(self, r):
        # показывает активную ячейку
        self.row = r

    def activatedRowColumn(self, r):
        if r not in self.list_of_extended_rows:
            self.table_w.setRowHeight(r, 100)
            self.list_of_extended_rows.append(r)
        else:
            self.table_w.setRowHeight(r, 35)
            self.list_of_extended_rows.remove(r)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())
