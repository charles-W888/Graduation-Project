# -*- coding: utf-8 -*-
"""
 @Time    : 2020/4/11 15:10
 @Author  : Charles
 @Project   : PyQt_learning
 @File    : runLoginWin.py
 @Software: PyCharm
 """
import sys
from appUI import loginWin
from appUI import registerWin

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWidget = QWidget()
    registerWidget = QWidget()

    ui = loginWin.Ui_Form()
    ui.setupUi(loginWidget)

    ui_2 = registerWin.Ui_Signup()
    ui_2.setupUi(registerWidget)

    loginWidget.show()

    ui.label_2.clicked.connect(loginWidget.close)  # 登录窗口关闭
    ui.label_2.clicked.connect(registerWidget.show)  # 注册窗口打开
    sys.exit(app.exec_())
