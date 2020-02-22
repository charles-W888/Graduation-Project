# -*- coding: utf-8 -*-
"""
 @Time    : 2020/2/20 21:07
 @Author  : Charles
 @Project : Gesture_Recognition
 @File    : gesture_rec.py
 @Software: PyCharm
"""
import cv2
from managers import WindowManager, CaptureManager


class GestureRecognition:
    def __init__(self):
        self._camera = cv2.VideoCapture(0)
        self._frameNum = 0
        self._windowManager = WindowManager('Gesture Detection', self.onKeypress)
        self._captureManager = CaptureManager(self._camera, self._windowManager, True)

    def run(self):
        """
          循环捕获下一帧，存入文件，释放帧。
          即不停地调用enterFrame()和exitFrame()。同时不停地扫描键盘输入。
        :return:
        """
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._frameNum += 1
            self._captureManager.enterFrame()

            # 帧差法去除背景
            if self._frameNum == 1:
                bgFrame = self._captureManager.frame
            if self._frameNum > 1:
                frame = self._captureManager.frame
                frame = cv2.subtract(bgFrame, frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """
          键盘处理函数，可用于监控
          空格：截图
          tab：录像
          Esc：退出监控（退出控制系统）
        :param keycode:
        :return:
        """
        if keycode == 32:  # space
            self._captureManager.writeImage('tempFile/screenshot.png')
        elif keycode == 9:  # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('tempFile/screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:  # Esc
            self._camera.release()
            self._windowManager.destroyWindow()
