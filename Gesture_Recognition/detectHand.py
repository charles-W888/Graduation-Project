# -*- coding: utf-8 -*-
"""
 @Time    : 2020/2/21 19:08
 @Author  : Charles
 @Project : Gesture_Recognition
 @File    : detectHand.py
 @Software: PyCharm
 通过肤色检测来探测手势，测试HSV，YCrCb两种色彩空间哪种更优
"""
import cv2
import numpy as np


class Detect:

    def __init__(self, capFrame):
        self._capFrame = capFrame
        self._hand = None

    def subBackground(self):
        """
        .  去除背景
        :return:
        """
        fgbg = cv2.createBackgroundSubtractorMOG2()
        fgmask = fgbg.apply(self._capFrame)

    def skinDetection_HSV(self):
        """
        .  使用HSV颜色空间进行肤色检测
        :return:
        """
        hsv = cv2.cvtColor(self._capFrame, cv2.COLOR_BGR2HSV)  # 把图像转换到HSV色域
        hsv = cv2.GaussianBlur(hsv, (7, 7), 0)
        # h, s, v = cv2.split(hsv)

        # # 肤色范围，色调值（H）在[5,170]之间，饱和度值（S）在[25,166]之间
        # minHue = 5
        # maxHue = 170
        # hueSkin = cv2.inRange(h, minHue, maxHue)
        # minSat = 25
        # maxSat = 166
        # satSkin = cv2.inRange(s, minSat, maxSat)
        # skin = hueSkin & satSkin
        # roi = cv2.bitwise_and(self._capFrame, self._capFrame, mask=skin)
        # return roi
        lower_skin = np.array([7, 20, 50])
        upper_skin = np.array([20, 250, 250])
        self._hand = cv2.inRange(hsv, lower_skin, upper_skin)

    def skinDetection_YCrCb1(self):
        """
        .  使用YCrCb即YUV颜色空间进行肤色检测
        :return:
        """
        ycrcb = cv2.cvtColor(self._capFrame, cv2.COLOR_BGR2YCrCb)  # 把图像转换到YCrCb色域

        # 高斯滤波
        ycrcb = cv2.GaussianBlur(ycrcb, (7, 7), 0)
        # 量化后，各分量范围为：y[16, 235]  u[16, 240]  v[16, 240] 。另外，黄种人皮肤Cr，Cb分量取值
        # 为133~173, 77~127
        lower_skin = np.array([16, 133, 77])
        upper_skin = np.array([235, 173, 127])
        self._hand = cv2.inRange(ycrcb, lower_skin, upper_skin)

    def skinDetection_YCrCb2(self):
        """
        .  对YCrCb颜色空间的Cr分量做阈值分割处理，使用Otsu阈值分割算法
        .  使用此方法无需再调用findHandContours()方法
        :return:
        """
        ycrcb = cv2.cvtColor(self._capFrame, cv2.COLOR_BGR2YCrCb)
        (y, cr, cb) = cv2.split(ycrcb)

        # 高斯滤波, cr 是待滤波的源图像数据, (5,5)是值窗口大小, 0 是指根据窗口大小来计算高斯函数标准差
        cr = cv2.GaussianBlur(cr, (7, 7), 0)

        # 根据OTSU算法求图像阈值, 对图像进行二值化
        _, skin = cv2.threshold(cr, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # 形态学处理：先进行开运算，再闭运算
        # 开运算是先腐蚀后膨胀，用于移出由图像噪音形成的斑点； 闭运算是先膨胀后腐蚀，用来连接被误分为许多小块的对象。
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        skin = cv2.morphologyEx(skin, cv2.MORPH_OPEN, kernel, iterations=2)
        # skin = cv2.morphologyEx(skin, cv2.MORPH_CLOSE, kernel, iterations=1)
        return skin

    def findEdges(self, img):
        # edge = cv2.Canny(img, 118, 200)
        _, contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        maxArea = 0
        maxId = 0
        for id, con in enumerate(contours):
            area = cv2.contourArea(con)
            if area > maxArea:
                maxArea = area
                maxId = id
        rect = cv2.minAreaRect(con)
        return img

    def findHandContours(self):
        """
        .  手的轮廓检测
        :return:
        """
        __handSrc = self._hand
        kernel = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(__handSrc, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        image, contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        correctContours = []
        for con in contours:
            if cv2.contourArea(con) > 9000:
                correctContours.append(con)
        for cocnt in correctContours:
            epsilon = 0.01 * cv2.arcLength(cocnt, True)
            approx = cv2.approxPolyDP(cocnt, epsilon, True)
            hull = cv2.convexHull(cocnt)
            cv2.drawContours(self._capFrame, [cocnt], -1, (0, 255, 0), 2)
            cv2.drawContours(self._capFrame, [approx], -1, (255, 0, 0), 2)
            cv2.drawContours(self._capFrame, [hull], -1, (0, 0, 255), 2)

            # drawing = np.zeros(self._capFrame.shape, np.uint8)
            # moments = cv2.moments(approx)  # 求出轮廓的各阶矩
            # center = (int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00']))
            # cv2.circle(drawing, center, 8, (0, 0, 255), -1)  # 画出重心

        return self._capFrame
