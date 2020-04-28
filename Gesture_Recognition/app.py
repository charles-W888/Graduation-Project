# -*- coding: utf-8 -*-
"""
 @Time    : 2020/2/21 17:13
 @Author  : Charles
 @Project : Gesture_Recognition
 @File    : app.py
 @Software: PyCharm
"""
import sys
from appUI import loginWin
from appUI import registerWin
from appUI import mainApp

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = mainApp.Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()

    # 登录和注册界面
    loginWidget = QWidget()
    registerWidget = QWidget()

    ui_L = loginWin.Ui_Form()
    ui_L.setupUi(loginWidget)

    ui_R = registerWin.Ui_Signup()
    ui_R.setupUi(registerWidget)

    ui.pushButton.clicked.connect(loginWidget.show)
    ui_L.label_2.clicked.connect(loginWidget.close)  # 登录窗口关闭
    ui_L.label_2.clicked.connect(registerWidget.show)  # 注册窗口打开
    sys.exit(app.exec_())
