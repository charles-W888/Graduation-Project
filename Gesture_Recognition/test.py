# -*- coding: utf-8 -*-
"""
 @Time    : 2020/2/21 19:43
 @Author  : Charles
 @Project : Gesture_Recognition
 @File    : test.py
 @Software: PyCharm
"""
import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    # https://www.cnblogs.com/demodashi/p/9437559.html
    # Idea1:  Based on YCrCb color space and Otsu threshold segmentation algorithm
    # ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)  # 把图像转换到YUV色域
    # (y, cr, cb) = cv2.split(ycrcb)  # 图像分割, 分别获取y, cr, br通道图像
    # # 高斯滤波, cr 是待滤波的源图像数据, (5,5)是值窗口大小, 0 是指根据窗口大小来计算高斯函数标准差
    # cr1 = cv2.GaussianBlur(cr, (5, 5), 0)  # 对cr通道分量进行高斯滤波
    # # 根据OTSU算法求图像阈值, 对图像进行二值化
    # _, skin1 = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #
    # cv2.imshow("image CR", cr1)
    # cv2.imshow("Skin1 Cr+OSTU", skin1)

    # Idea2:  Cr, Cb range screening method based on YCrCb color space
    # 正常黄种人的Cr分量大约在140至175之间，Cb分量大约在100至120之间。
    # ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)  # 把图像转换到YUV色域
    # (y, cr, cb) = cv2.split(ycrcb)  # 图像分割, 分别获取y, cr, br通道分量图像
    #
    # skin2 = np.zeros(cr.shape, dtype=np.uint8)  # 根据源图像的大小创建一个全0的矩阵,用于保存图像数据
    # (x, y) = cr.shape  # 获取源图像数据的长和宽
    #
    # # 遍历图像, 判断Cr和Br通道的数值, 如果在指定范围中, 则把新图像的点设为255,否则设为0
    # for i in range(0, x):
    #     for j in range(0, y):
    #         if (cr[i][j] > 140) and (cr[i][j] < 175) and (cb[i][j] > 100) and (cb[i][j] < 120):
    #             skin2[i][j] = 255
    #         else:
    #             skin2[i][j] = 0
    # cv2.imshow("Skin2 Cr+Cb", skin2)

    # Idea3:  H, S, V range filtering based on HSV color space
    # 正常黄种人的H分量大约在7至20之间，S分量大约在28至256之间，V分量大约在50至256之间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 把图像转换到HSV色域
    (_h, _s, _v) = cv2.split(hsv)  # 图像分割, 分别获取h, s, v 通道分量图像
    skin3 = np.zeros(_h.shape, dtype=np.uint8)  # 根据源图像的大小创建一个全0的矩阵,用于保存图像数据
    (x, y) = _h.shape  # 获取源图像数据的长和宽

    # 遍历图像, 判断HSV通道的数值, 如果在指定范围中, 则置把新图像的点设为255,否则设为0
    for i in range(0, x):
        for j in range(0, y):
            if (_h[i][j] > 7) and (_h[i][j] < 20) and (_s[i][j] > 28) and (_s[i][j] < 255) and (_v[i][j] > 50) and (
                    _v[i][j] < 255):
                skin3[i][j] = 255
            else:
                skin3[i][j] = 0

    cv2.imshow("Skin3 HSV", skin3)

    if cv2.waitKey(1000 // 12) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
