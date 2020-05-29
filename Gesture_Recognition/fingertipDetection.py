# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/29 13:12
 @Author  : Charles
 @Project   : Gesture_Recognition
 @File    : fingertipDetection.py
 @Software: PyCharm
 """
import cv2


def detectFinger(hand, contours):
    # 计算图像的矩
    moments = cv2.moments(hand)
    # hu_moments = cv2.HuMoments(moments)

    # 计算图像的重心
    fx = int(moments['m10'] / moments['m00'])
    fy = int(moments['m01'] / moments['m00'])
    maxDist = 0
    fingertip = 0
    for i, j in contours:
        dist = (i - fx) ** 2 + (j - fy) ** 2
        if dist > maxDist:
            maxDist = dist
            fingertip = (i, j)
    return fingertip

def getFingerPos(point):
    pass
