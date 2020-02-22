# -*- coding: utf-8 -*-
"""
 @Time    : 2020/2/21 17:13
 @Author  : Charles
 @Project : Gesture_Recognition
 @File    : app.py
 @Software: PyCharm
"""
import gesture_rec
import sys
from appUI import loginWin
from appUI import registerWin

from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    # gest_rec = gesture_rec.GestureRecognition()
    # gest_rec.run()
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
