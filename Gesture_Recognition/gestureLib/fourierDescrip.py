# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/12 19:28
 @Author  : Charles
 @Project   : Gesture_Recognition
 @File    : fourierDescrip.py
 @Software: PyCharm
 """
import cv2
import numpy as np

MIN_DESCRIPTOR = 32


def fourierDescriptor(res):
    """
    进行傅里叶变换
    :param res: 灰度图
    :return: null
    """
    contours = find_coutours(res)  # 提取轮廓点坐标
    con_list = contours[0][:, 0, :]  #只保留区域面积最大的轮廓点坐标
    con_complex = np.empty(con_list.shape[:-1], dtype=complex)
    con_complex.real = con_list[:, 0]  # 横坐标作为实数部分
    con_complex.imag = con_list[:, 1]  # 纵坐标作为虚数部分
    fourier_ret = np.fft.fft(con_complex)  # 傅里叶变换
    descriptor_in_use = truncate_descriptor(fourier_ret)
    return descriptor_in_use, con_list

def find_coutours(img):
    _, contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    return contours

def truncate_descriptor(fourier_ret):
    """
    截断傅里叶描述子
    :param fourier_ret:
    :return:
    """
    descriptors_in_use = np.fft.fftshift(fourier_ret)
    center_index = int(len(descriptors_in_use) / 2)
    low, high = center_index - int(MIN_DESCRIPTOR / 2), center_index + int(MIN_DESCRIPTOR / 2)
    descriptors_in_use = descriptors_in_use[low:high]
    descriptors_in_use = np.fft.ifftshift(descriptors_in_use)
    return descriptors_in_use
