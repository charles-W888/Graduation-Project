# -*- coding: utf-8 -*-
"""
 @Time    : 2/8/2020 7:11 PM
 @Author  : Charles
 @Project : Cameo(Facial Tracking)
 @File    : cameo.py
 @Software: PyCharm
"""
import cv2
import filters
from managers import WindowManager, CaptureManager


class Cameo:
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        self._curveFilter = filters.BGRPortraCurveFilter()

    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            filters.strokeEdges(frame, frame)
            self._curveFilter.apply(frame, frame)

            # TODO: Filter the frame (Chapter 3)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """Handle a keypress.
        space   -> Take a screenshot.
        tab     -> Start/Stop recording a screencast.
        escape  -> Quit.
        """
        if keycode == 32:  # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:  # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:  # Esc
            self._windowManager.destroyWindow()


cameo = Cameo()
cameo.run()
