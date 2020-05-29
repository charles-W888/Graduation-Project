# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/28 16:24
 @Author  : Charles
 @Project   : Gesture_Recognition
 @File    : RecogandControl.py
 @Software: PyCharm
 """
import time
import win32api
import win32con


def mouse_event_respon(x, y, label=0):
    """
    鼠标响应事件
    :param label:   事件类型
    :param x:  鼠标x轴坐标
    :param y: 鼠标y轴坐标
    :return: null
    """
    mouse_move(x, y)
    if label == 0:
        return None
    if label == 2:  # 左键按下
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    if label == 3:  # 左键按下两次
        times = 2
        time.sleep(0.05)
        while times:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            times -= 1
    if label == 4:  # 右键按下
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

def mouse_move(x, y):
    """
    鼠标移动
    :param x:  移动位置x坐标
    :param y:  移动位置y坐标
    :return:  null
    """
    if x is not None and y is not None:
        point = (x, y)
        win32api.SetCursorPos(point)
