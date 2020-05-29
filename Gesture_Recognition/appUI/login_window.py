# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form, user):
        self.__user = user
        Form.setObjectName("Form")
        Form.resize(340, 473)
        Form.setFixedSize(340, 473)
        # 窗口居中
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = Form.geometry()
        Form.move(
            (screen.width() - size.width()) / 2,
            (screen.height() - size.height()) / 2
        )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Graduate-Design\\Graduation-Project\\"
                                     "Gesture_Recognition\\img\\图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(True)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QtGui.QPixmap(
            "D:\\Graduate-Design\\Graduation-Project\\Gesture_Recognition\\img\\图片2.png")))
        Form.setPalette(palette)
        self.uname = QtWidgets.QLabel(Form)
        self.uname.setEnabled(True)
        self.uname.setGeometry(QtCore.QRect(30, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.uname.setFont(font)
        self.uname.setObjectName("uname")
        self.lineEdit_u = QtWidgets.QLineEdit(Form)
        self.lineEdit_u.setGeometry(QtCore.QRect(30, 230, 281, 35))
        self.lineEdit_u.setStyleSheet("border-radius: 4px;")
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.lineEdit_u.setFont(font)
        self.lineEdit_u.setObjectName("lineEdit_u")
        self.psw = QtWidgets.QLabel(Form)
        self.psw.setGeometry(QtCore.QRect(30, 280, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.psw.setFont(font)
        self.psw.setObjectName("psw")
        self.lineEdit_p = QtWidgets.QLineEdit(Form)
        self.lineEdit_p.setGeometry(QtCore.QRect(30, 310, 281, 35))
        self.lineEdit_p.setStyleSheet("border-radius: 4px;")
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.lineEdit_p.setFont(font)
        self.lineEdit_p.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_p.setObjectName("lineEdit_p")
        self.pushButton = MyButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 370, 281, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 190, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 190, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 190, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                        "background-color: rgb(47, 190, 80); border: 2px groove gray;"
                                      "border-radius: 4px; padding: 2px 4px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClick)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(61, 420, 101, 21))
        self.label.setCursor(QtCore.Qt.IBeamCursor)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QPushButton(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 420, 111, 21))
        self.label_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_2.setStyleSheet("color: rgb(0, 0, 255); background: transparent;")
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_2.setFont(font)
        self.label_2.setObjectName("linkBtn")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(90, 150, 160, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(103, 103, 103);")
        self.title.setCursor(QtCore.Qt.IBeamCursor)
        self.title.setObjectName("title")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setEnabled(True)
        self.logo.setGeometry(QtCore.QRect(90, 10, 155, 155))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("D:\\Graduate-Design\\Graduation-Project\\"
                                          "Gesture_Recognition\\img\\图标.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.uname.setText(_translate("Form", "Username"))
        self.psw.setText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Sign in"))
        self.label.setText(_translate("Form", "New to HANKit?"))
        self.label_2.setText(_translate("Form", "Create an account."))
        self.title.setText(_translate("Form", "Sign in to HANKit"))

    def onClick(self):
        print("Click the button.")
        username = self.uname.text()
        passwd = self.psw.text()
        if self.__user.user_login(username, passwd):
            print('Login OK')
            reply = QtWidgets.QMessageBox.information(self, "Check Box", "Success Log in!")
            self.uname.setText("")
            self.psw.setText("")
            self.close()
        else:
            reply = QtWidgets.QMessageBox.warning(self, 'Check Box', 'Fail Log!')
        self.__user.closeDB()


class MyButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(MyButton, self).__init__(parent)

    def enterEvent(self, a0: QtCore.QEvent):
        self.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(42, 171, 70); border: 1px groove rgb(90, 90, 90);"
                                      "border-radius: 4px; padding: 2px 4px;")

    def leaveEvent(self, a0: QtCore.QEvent):
        self.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(47, 190, 80); border: 2px groove gray;"
                                      "border-radius: 4px; padding: 2px 4px;")
