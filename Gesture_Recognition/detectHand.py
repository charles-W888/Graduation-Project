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

    def skinDetection_HSV(self):
        """
        .  使用HSV颜色空间进行肤色检测
        :return:
        """
        hsv = cv2.cvtColor(self._capFrame, cv2.COLOR_BGR2HSV)  # 把图像转换到HSV色域
        lower_skin = np.array([7, 20, 50])
        upper_skin = np.array([20, 255, 255])
        self._hand = cv2.inRange(hsv, lower_skin, upper_skin)

    def skinDetection_YCrCb1(self):
        """
        .  使用YCrCb即YUV颜色空间进行肤色检测
        :return:
        """
        ycrcb = cv2.cvtColor(self._capFrame, cv2.COLOR_BGR2YCrCb)  # 把图像转换到YCrCb色域
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
        cr = cv2.GaussianBlur(cr, (5, 5), 0)

        # 根据OTSU算法求图像阈值, 对图像进行二值化
        _, skin = cv2.threshold(cr, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return skin

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
                correctContours.append(cv2.convexHull(con))
        cv2.drawContours(self._capFrame, correctContours, -1, (0, 255, 0), 2)
        return self._capFrame
