# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainApp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import cv2
from datetime import datetime
import numpy as np
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget

from detect_hand import Detect
import fingertipDetection as fgdt
import gestureLib.fourierDescrip as fd
from gestureLib.gesture_svm import ClassifierSVM
import RecogandControl as rc


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.timer_camera = QtCore.QTimer()
        self.camera = cv2.VideoCapture()
        # self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # DSHOW用于解决[ WARN:1] terminating async callback
        self.timer_camera.timeout.connect(self.show_cam)
        self.res = set()
        self.seed = random.randint(1, 3)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.setFixedSize(1000, 600)
        self.setWindowIcon(QtGui.QIcon("img/图标.png"))

        # 窗口居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 1000, 611))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)  # 显示手原始图像
        self.label_2.setGeometry(QtCore.QRect(80, 90, 301, 301))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setScaledContents(True)
        self.label_3 = QtWidgets.QLabel(self.page)  # 显示手轮廓图
        self.label_3.setGeometry(QtCore.QRect(600, 90, 301, 301))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(113, 40, 231, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(660, 40, 231, 21))
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 451, 461))
        self.label_6.setStyleSheet("background-color: rgb(0, 199, 140);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.startPushButton = QtWidgets.QPushButton(self.page_2)
        self.startPushButton.setGeometry(QtCore.QRect(600, 40, 71, 31))
        self.startPushButton.setObjectName("startPushButton")
        self.startPushButton.setStyleSheet("color: rgb(255, 255, 255); background-color: red")
        font = QtGui.QFont()
        font.setFamily("Microsoft Ya Hei")
        font.setPointSize(10)
        self.startPushButton.setFont(font)
        self.startPushButton.clicked.connect(self.playGames)

        self.stopPushButton = QtWidgets.QPushButton(self.page_2)
        self.stopPushButton.setGeometry(QtCore.QRect(600, 80, 71, 31))
        self.stopPushButton.setObjectName("stopPushButton")
        self.stopPushButton.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(88, 87, 86)")
        font = QtGui.QFont()
        font.setFamily("Microsoft Ya Hei")
        font.setPointSize(10)
        self.stopPushButton.setFont(font)
        self.stopPushButton.clicked.connect(self.stopGames)

        self.lcdNumber = QtWidgets.QLCDNumber(self.page_2)
        self.lcdNumber.setGeometry(QtCore.QRect(793, 30, 101, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(703, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(600, 120, 301, 301))
        self.label_8.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(210, 0, 101, 35))
        self.label_9.setStyleSheet("color: red")
        self.label_9.setObjectName("label_9")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setBold(True)
        font.setItalic(True)
        font.setPointSize(15)
        self.label_9.setFont(font)

        self.stackedWidget.addWidget(self.page_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 0, 80, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QPushButton(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(809, 0, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open_video)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile_F = QtWidgets.QMenu(self.menubar)
        self.menuFile_F.setObjectName("menuFile_F")
        self.menuGames_G = QtWidgets.QMenu(self.menubar)
        self.menuGames_G.setObjectName("menuGames_G")
        self.menuHelp_H = QtWidgets.QMenu(self.menubar)
        self.menuHelp_H.setObjectName("menuHelp_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionView_History_V = QtWidgets.QAction(MainWindow)
        self.actionView_History_V.setObjectName("actionView_History_V")

        self.actionSettings_S = QtWidgets.QAction(MainWindow)
        self.actionSettings_S.setObjectName("actionSettings_S")
        self.actionSettings_S.triggered.connect(self.switch1)

        self.actionExit_X = QtWidgets.QAction(MainWindow)
        self.actionExit_X.setObjectName("actionExit_X")
        self.actionExit_X.triggered.connect(QtWidgets.qApp.quit)
        self.actionRock_Paper_Scissors_R = QtWidgets.QAction(MainWindow)
        self.actionRock_Paper_Scissors_R.setObjectName("actionRock_Paper_Scissors_R")
        self.actionRock_Paper_Scissors_R.triggered.connect(self.switch)

        self.actionoperation_instructions_O = QtWidgets.QAction(MainWindow)
        self.actionoperation_instructions_O.setObjectName("actionoperation_instructions_O")
        self.menuFile_F.addAction(self.actionView_History_V)
        self.menuFile_F.addAction(self.actionSettings_S)
        self.menuFile_F.addSeparator()
        self.menuFile_F.addAction(self.actionExit_X)
        self.menuGames_G.addAction(self.actionRock_Paper_Scissors_R)
        self.menuHelp_H.addAction(self.actionoperation_instructions_O)
        self.menubar.addAction(self.menuFile_F.menuAction())
        self.menubar.addAction(self.menuGames_G.menuAction())
        self.menubar.addAction(self.menuHelp_H.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HANKit-EveryNontouch"))
        self.label_4.setText(_translate("MainWindow", "Please put your hand to this windows"))
        self.label_5.setText(_translate("MainWindow", "The outline of your hand"))
        self.label_7.setText(_translate("MainWindow", "Your Score"))
        self.label_9.setText(_translate("MainWindow", "Fighting!"))
        self.pushButton.setText(_translate("MainWindow", "Log in"))
        self.label.setText(_translate("MainWindow", "Predict"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.startPushButton.setText(_translate("MainWindow", "START!"))
        self.stopPushButton.setText(_translate("MainWindow", "Clear"))
        self.menuFile_F.setTitle(_translate("MainWindow", "File(&F)"))
        self.menuGames_G.setTitle(_translate("MainWindow", "Games(&G)"))
        self.menuHelp_H.setTitle(_translate("MainWindow", "Help(&H)"))
        self.actionView_History_V.setText(_translate("MainWindow", "View History(&V)"))
        self.actionSettings_S.setText(_translate("MainWindow", "Interaction(&I)"))
        self.actionExit_X.setText(_translate("MainWindow", "Exit(&X)"))
        self.actionRock_Paper_Scissors_R.setText(_translate("MainWindow", "Rock Paper Scissors(&R)"))
        self.actionoperation_instructions_O.setText(_translate("MainWindow", "operation instructions(&O)"))

    def switch(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch1(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_cam(self):
        width, height = 300, 300
        x0, y0 = 0, 0  # ROI选取位置
        _, self._frame = self.camera.read()
        self._detect = Detect(self._frame)
        self.origin_roi = self._detect.cutROI(self._frame, x0, y0, width, height)
        self.origin_roi = np.fliplr(self.origin_roi).copy()
        show = cv2.cvtColor(self.origin_roi, cv2.COLOR_BGR2RGB)
        showImg = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(showImg))

        self._roi = self._detect.skinDetection_YCrCb2()
        # self._roi = self._detect.findEdges(self._roi)
        self.mirroredROI = np.fliplr(self._roi).copy()
        showROI = QtGui.QImage(self.mirroredROI.data, self.mirroredROI.shape[1], self.mirroredROI.shape[0], QtGui.QImage.Format_Grayscale8)
        self.label_3.setPixmap(QtGui.QPixmap.fromImage(showROI))

        self.label_8.setPixmap(QtGui.QPixmap.fromImage(showROI))

        _, contours = fd.fourierDescriptor(self.mirroredROI)
        (self.x, self.y) = fgdt.detectFinger(self.mirroredROI, contours)  # 找到指尖位置
        rc.mouse_move(self.x * 8, self.y * 4)

        # self.recognition_gesture()

    def open_video(self):
        if self.timer_camera.isActive() == False:
            self.camera.open(0, cv2.CAP_DSHOW)

            if self.camera == False:
                msg = QtWidgets.QMessageBox.warning(self, 'warning!', 'Please check your computer camera', buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)
                self.pushButton_2.setText('Close')

        else:
            self.timer_camera.stop()
            self.camera.release()
            self.label_2.clear()
            self.label_3.clear()
            self.pushButton_2.setText('Open')
            self.write_log()

    def recognition_gesture(self):
        fourier_ret, _ = fd.fourierDescriptor(self._roi)
        descriptor_in_use = abs(fourier_ret)
        fd_test = np.zeros((1, 31))
        temp = descriptor_in_use[1]
        for k in range(1, len(descriptor_in_use)):
            fd_test[0, k - 1] = int(100 * descriptor_in_use[k] / temp)
        classifiersvm = ClassifierSVM()
        test_svm = classifiersvm.test_fd(fd_test)

        self.res.add(test_svm[0])
        print(self.res)
        rc.mouse_event_respon(self.x, self.y, label=test_svm[0])

    def write_log(self):
        cur_time = datetime.now()
        utc_time = cur_time.strftime("%Y-%m-%d")
        with open('recog.log', 'a+') as f:
            f.write(utc_time)
            f.write('\n')
            f.write('=======================\n')
            for l in self.res:
                content = ': Recognition label-' + l + '\n'
                f.write(content)
            f.write('=======================\n')
            f.close()

    def playGames(self):
        self.label_6.setPixmap(QtGui.QPixmap('img/fist.png'))
        self.label_6.setScaledContents(True)

    def stopGames(self):
        self.label_6.clear()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm Exit', "Are you sure you want to exit HANKit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.camera.isOpened():
                self.camera.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()
        else:
            event.ignore()
