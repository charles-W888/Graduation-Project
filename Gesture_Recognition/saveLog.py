# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/29 21:17
 @Author  : Charles
 @Project   : Gesture_Recognition
 @File    : saveLog.py
 @Software: PyCharm
 """
from datetime import datetime


def write_log(res):
    cur_time = datetime.now()
    utc_time = cur_time.strftime("%Y-%m-%d")
    with open('recog.log', 'a+') as f:
        f.write(utc_time)
        f.write('\n')
        f.write('=======================\n')
        for l in res:
            content = ': Recognition label-' + str(l) + '\n'
            f.write(content)
        f.write('=======================\n')
        f.close()
