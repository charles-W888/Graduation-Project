# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/10 14:26
 @Author  : Charles
 @Project   : Gesture_Recognition
 @File    : compute_feature.py
 @Software: PyCharm
 """
import os

loadPath = '../handImg'


def featureWrite():
    with open('feature.txt', 'w+') as f:
        for i, j, k in os.walk(loadPath):
            for f_name in k:
                a, _ = f_name.split('_')
                f.write(f_name + ':' + a + '\n')
        f.close()


# if __name__ == '__main__':
#     featureWrite()
