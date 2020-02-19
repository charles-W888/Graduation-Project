# -*- coding: utf-8 -*-
"""
 @Time    : 2020/2/15 22:14
 @Author  : Charles
 @Project : Cameo(Facial Tracking)
 @File    : filters.py
 @Software: PyCharm
 主要是滤波函数和类
"""
import cv2
import numpy as np
import utils


def strokeEdges(src, dst, blurKsize=7, edgeKsize=5):
    if blurKsize >= 3:
        blurredSrc = cv2.medianBlur(src, blurKsize)  # 模糊图像，去除噪声
        graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
    else:
        graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # ddepth = cv2.CV_8U表示每个通道为8位，若为负值，则表示目标图像额源图像有同样的位深度
    cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize=edgeKsize)  # 边缘检测
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha
    cv2.merge(channels, dst)


class BGRFuncFilter:
    def __init__(self, vFunc=None, bFunc=None, gFunc=None, rFunc=None, dtype=np.uint8):
        length = np.iinfo(dtype).max + 1
        self._bLookupArray = utils.createLookupArray(utils.createCompositeFunc(bFunc, vFunc), length)
        self._gLookupArray = utils.createLookupArray(utils.createCompositeFunc(gFunc, vFunc), length)
        self._rLookupArray = utils.createLookupArray(utils.createCompositeFunc(rFunc, vFunc), length)

    def apply(self, src, dst):
        """
        . Apply the filter with a BGR source/destination.
        :param src:
        :param dst:
        :return:
        """
        b, g, r = cv2.split(src)
        utils.applyLookupArray(self._bLookupArray, b, b)
        utils.applyLookupArray(self._gLookupArray, g, g)
        utils.applyLookupArray(self._rLookupArray, r, r)
        cv2.merge([b, g, r], dst)


class BGRCurveFilter(BGRFuncFilter):
    def __init__(self, vPoints=None, bPoints=None, gPoints=None, rPoints=None, dtype=np.uint8):
        BGRFuncFilter.__init__(self, utils.createCurveFunc(vPoints), utils.createCurveFunc(bPoints),
                               utils.createCurveFunc(gPoints), utils.createCurveFunc(rPoints), dtype)


class BGRPortraCurveFilter(BGRCurveFilter):
    def __init__(self, dtype=np.uint8):
        BGRCurveFilter.__init__(
            self,
            vPoints=[(0, 0), (23, 20), (157, 173), (255, 255)],
            bPoints=[(0, 0), (41, 46), (231, 228), (255, 255)],
            gPoints=[(0, 0), (52, 47), (189, 196), (255, 255)],
            rPoints=[(0, 0), (69, 69), (213, 218), (255, 255)],
            dtype=dtype
        )


class VConvolutionFilter:
    """
    . A filter that applies a convolution to V (or all of BGR).
    . 表示一般的卷积滤波器
    """

    def __init__(self, kernel):
        self._kernel = kernel

    def apply(self, src, dst):
        """
        . Apply the filter with a BGR or gray source/destination.
        :param src:
        :param dst:
        :return:
        """
        cv2.filter2D(src, -1, self._kernel, dst)


class SharpenFilter(VConvolutionFilter):
    """
    . A sharpen filter with a 1-pixel radius.
    . 表示特定的锐化滤波器
    """

    def __init__(self):
        kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class FindEdgesFilter(VConvolutionFilter):
    """
    . An edge-finding filter with a 1-pixel radius.
    . 边缘检测滤波器
    """

    def __init__(self):
        kernel = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class BlurFilter(VConvolutionFilter):
    """
    . A blur filter with 2-pixel radius.
    . 模糊滤波器，此类实现了一个简单的邻近平均滤波器
    """

    def __init__(self):
        kernel = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04]])
        VConvolutionFilter.__init__(self, kernel)


class EmbossFilter(VConvolutionFilter):
    """
    . An emboss filter with a 1-pixel radius.
    . 不对称的核，同时具有模糊（正权重）和锐化（负权重）的作用，
    . 会产生一种脊状或浮雕效果。
    """

    def __init__(self):
        kernel = np.array([[-2, -1, 0],
                           [-1,  1, 1],
                           [ 0,  1, 2]])
        VConvolutionFilter.__init__(self, kernel)
