# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush


class Ui_Signup(object):
    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.resize(450, 561)
        Signup.setFixedSize(450, 561)
        # 窗口居中
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = Signup.geometry()
        Signup.move(
            (screen.width() - size.width()) / 2,
            (screen.height() - size.height()) / 2
        )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Graduate-Design\\Graduation-Project\\"
                                     "Gesture_Recognition\\img\\图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Signup.setWindowIcon(icon)
        Signup.setAutoFillBackground(True)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QtGui.QPixmap(
            "D:\\Graduate-Design\\Graduation-Project\\Gesture_Recognition\\img\\图片2-1.png")))
        Signup.setPalette(palette)
        self.label = QtWidgets.QLabel(Signup)
        self.label.setGeometry(QtCore.QRect(180, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(100, 100, 100);")
        self.label.setObjectName("label")
        self.label.setCursor(QtCore.Qt.IBeamCursor)
        self.label_2 = QtWidgets.QLabel(Signup)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setCursor(QtCore.Qt.IBeamCursor)
        self.label_3 = QtWidgets.QLabel(Signup)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Signup)
        self.label_4.setGeometry(QtCore.QRect(108, 132, 54, 12))
        self.label_4.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.unameEdit = QtWidgets.QLineEdit(Signup)
        self.unameEdit.setGeometry(QtCore.QRect(40, 165, 371, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.unameEdit.setFont(font)
        self.unameEdit.setObjectName("unameEdit")
        self.label_5 = QtWidgets.QLabel(Signup)
        self.label_5.setGeometry(QtCore.QRect(105, 227, 54, 12))
        self.label_5.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Signup)
        self.label_6.setGeometry(QtCore.QRect(40, 225, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pswEdit = QtWidgets.QLineEdit(Signup)
        self.pswEdit.setGeometry(QtCore.QRect(40, 260, 371, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.pswEdit.setFont(font)
        self.pswEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pswEdit.setObjectName("pswEdit")
        self.label_7 = QtWidgets.QLabel(Signup)
        self.label_7.setGeometry(QtCore.QRect(145, 322, 54, 12))
        self.label_7.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Signup)
        self.label_8.setGeometry(QtCore.QRect(40, 322, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.vpswEdit = QtWidgets.QLineEdit(Signup)
        self.vpswEdit.setGeometry(QtCore.QRect(40, 357, 371, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.vpswEdit.setFont(font)
        self.vpswEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.vpswEdit.setObjectName("vpswEdit")
        self.tip_up = QtWidgets.QLabel(Signup)
        self.tip_up.setGeometry(QtCore.QRect(40, 405, 371, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.tip_up.setFont(font)
        self.tip_up.setObjectName("tip_up")
        self.tip_up.setCursor(QtCore.Qt.IBeamCursor)
        self.tip_down = QtWidgets.QLabel(Signup)
        self.tip_down.setGeometry(QtCore.QRect(40, 420, 371, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.tip_down.setFont(font)
        self.tip_down.setObjectName("tip_down")
        self.tip_down.setCursor(QtCore.Qt.IBeamCursor)
        self.pushButton = QtWidgets.QPushButton(Signup)
        self.pushButton.setGeometry(QtCore.QRect(40, 460, 371, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(16, 116, 231);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.clicked.connect(self.sign_up)

        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Join HANKit"))
        self.label.setText(_translate("Signup", "Join HANKit"))
        self.label_2.setText(_translate("Signup", "Create your account"))
        self.label_3.setText(_translate("Signup", "Username"))
        self.label_4.setText(_translate("Signup", "*"))
        self.label_5.setText(_translate("Signup", "*"))
        self.label_6.setText(_translate("Signup", "Password"))
        self.label_7.setText(_translate("Signup", "*"))
        self.label_8.setText(_translate("Signup", "Verify Password"))
        self.tip_up.setText(_translate("Signup", "Make sure it\'s at least 15 characters OR at least 8 characters"))
        self.tip_down.setText(_translate("Signup", "including a number and a lowercase letter."))
        self.pushButton.setText(_translate("Signup", "Sign Up"))

    def sign_up(self):
        print("click the Sign up button.")
