# -*- coding: utf-8 -*-
"""
 @Time    : 2/8/2020 3:28 PM
 @Author  : Charles
 @Project : Gesture_Recognition
 @File    : managers.py
 @Software: PyCharm
"""
import cv2
import numpy as np
import time

from detectHand import Detect


# 用于视频图像管理。读取新的帧，将帧分派到一个或多个输出中
class CaptureManager:
    def __init__(self, capture, previewWindowManager=None, shouldMirrorPreview=False):
        self.previewWindowManager = previewWindowManager  # 传入一个WindowManager类，即输出窗口
        self.shouldMirrorPreview = shouldMirrorPreview  # 是否镜像显示

        # 单下划线代表是保护变量（只有类对象和子类对象能访问）  self._XXX是实例变量
        self._capture = capture  # 此参数传入一个输入的视频流，比如电脑摄像头
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None

        self._startTime = None
        self._framesElapsed = int(0)

        # fps，每秒传输帧数
        self._fpsEstimate = None

        # 用于标记当前是第几帧
        # self._frameNum = 0

        # 传入一个Detect对象用于手的检测
        self._detect = None

    # 设置只读属性
    @property
    def channel(self):
        return self._channel

    # 设置可写属性
    @channel.setter
    def channel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None

    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            # _, self._frame = self._capture.retrieve()
            _, self._frame = self._capture.read()
            # self._frameNum += 1
            # if self._frameNum == 1:
            #     print('1')
            # elif self._frameNum > 1:
            #     print(self._frameNum)
            self._detect = Detect(self._frame)

            # Idea1： Based on the HSV color space  效果最差
            # self._detect.skinDetection_HSV()
            # self._frame = self._detect.findHandContours()

            # # Idea2： Based on the YCrCb color space
            # self._detect.skinDetection_YCrCb1()
            # self._frame = self._detect.findHandContours()

            # Idea3： Based on the YCrCb color space and Otsu threshold segmentation algorithm  效果最好
            self._frame = self._detect.skinDetection_YCrCb2()
            self._frame = self._detect.findEdges(self._frame)
        return self._frame

    @property
    def isWritingImage(self):
        return self._imageFilename is not None

    @property
    def isWritingVideo(self):
        return self._videoFilename is not None

    def enterFrame(self):
        """捕获下一帧。用于启动摄像头录制功能"""

        """在这之前，检查是否有之前的帧未退出。如果有，给出提示
        assert not self._enteredFrame, 'previous enterFrame() had no matching exitFrame()'"""
        if self._capture is not None:
            self._enteredFrame = self._capture.grab()

    def exitFrame(self):
        """写入文件并释放帧
        .  此类中的核心函数，实现了视频显示、视频录制和截图保存的功能
        """

        """从当前通道获取图像，估计帧速率，显示图像，执行暂停的请求，写入(保存)图像
        .  检查是否有捕获的帧是可获取的。
        .  取值器（the getter）可能获取并缓存帧
        """
        if self.frame is None:
            self._enteredFrame = False
            return

        # 更新fps估算值和相关变量。
        if self._framesElapsed == 0:
            self._startTime = time.time()
        else:
            timeElapsed = time.time() - self._startTime
            self._fpsEstimate = self._framesElapsed / timeElapsed
        self._framesElapsed += 1

        # 展示图像
        if self.previewWindowManager is not None:
            if self.shouldMirrorPreview:

                # 向左 / 右方向翻转阵列，即翻转图像
                mirroredFrame = np.fliplr(self._frame).copy()
                self.previewWindowManager.show(mirroredFrame)
            else:
                self.previewWindowManager.show(self._frame)

        # 将图像写入文件
        if self.isWritingImage:
            cv2.imwrite(self._imageFilename, self._frame)
            self._imageFilename = None

        # 将录像写入文件
        self._writeVideoFrame()

        # 释放帧
        self._frame = None
        self._enteredFrame = False

    def writeImage(self, filename):
        """将下一个退出的帧写入图像文件。设置图像的文件名"""
        self._imageFilename = filename

    def startWritingVideo(self, filename, encoding=cv2.VideoWriter_fourcc('I', '4', '2', '0')):
        """开始录制"""
        self._videoFilename = filename
        self._videoEncoding = encoding

    def stopWritingVideo(self):
        """停止录制"""
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None

    def _writeVideoFrame(self):
        """录制视频"""
        if not self.isWritingVideo:
            return
        if self._videoWriter is None:
            fps = self._capture.get(cv2.CAP_PROP_FPS)
            if fps == 0.0:
                # 由于捕获摄像头的fps未知，因此使用估计值
                if self._framesElapsed < 20:
                    # 检查尽可能多的帧，以使估计更准确。
                    return
                else:
                    fps = self._fpsEstimate
            size = (int(self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            self._videoWriter = cv2.VideoWriter(self._videoFilename, self._videoEncoding, fps, size)
            self._videoWriter.write(self._frame)


# 用于界面管理。以面向对象的形式处理窗口和事件
class WindowManager:
    def __init__(self, windowName, keypressCallback=None):
        self.keypressCallback = keypressCallback
        self._windowName = windowName
        self._isWindowCreated = False

        # self.app = QApplication(sys.argv)
        # self.mainWin = QMainWindow()
        # self.ui = None

    @property
    def isWindowCreated(self):
        return self._isWindowCreated

    def createWindow(self):
        """创建窗口"""

        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True

    def show(self, frame):
        """显示窗口"""

        cv2.imshow(self._windowName, frame)
        # self.ui = mainApp.Ui_MainWindow(frame)
        # self.ui.setupUi(self.mainWin)
        # self.mainWin.show()
        # sys.exit(self.app.exec_())

    def destroyWindow(self):
        """注销窗口"""

        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False

    def processEvents(self):
        """执行键盘操作的回调函数"""

        # 等待键盘输入,括号中的参数表示等待时间,单位毫秒。0表示无限期等待
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            # Discard any non-ASCII info encoded by GTK.
            keycode &= 0xFF
            self.keypressCallback(keycode)
