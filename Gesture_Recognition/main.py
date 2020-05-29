# -*- coding: utf-8 -*-
"""
 @Time    : 2020/2/21 17:13
 @Author  : Charles
 @Project : Gesture_Recognition
 @File    : main.py
 @Software: PyCharm
"""
import sys
from models import users
from appUI import login_window
from appUI import register_window
from appUI import main_window
from appUI import history

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()

    # 登录和注册界面
    loginWidget = QWidget()
    registerWidget = QWidget()

    user = users.User()
    user.createTable()

    ui_L = login_window.Ui_Form()
    ui_L.setupUi(loginWidget, user)

    ui_R = register_window.Ui_Signup()
    ui_R.setupUi(registerWidget, user)

    ui.pushButton.clicked.connect(loginWidget.show)
    ui_L.label_2.clicked.connect(loginWidget.close)  # 登录窗口关闭
    ui_L.label_2.clicked.connect(registerWidget.show)  # 注册窗口打开

    historyWin = QDialog()
    hiW = history.Ui_Dialog()
    hiW.setupUi(historyWin)
    ui.actionView_History_V.triggered.connect(historyWin.show)

    sys.exit(app.exec_())
