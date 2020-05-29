# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/10 11:03
 @Author  : Charles
 @Project   : Gesture_Recognition
 @File    : lib_expand.py
 @Software: PyCharm
 """
import random
import cv2

path = 'handImg/'
write_path = 'test_img/'


def rotate(img, scale=0.9):
    angle = random.randrange(-90, 90)
    w = img.shape[1]
    h = img.shape[0]

    # rotate matrix
    M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, scale)
    # rotate
    img = cv2.warpAffine(img, M, (w, h))
    return img


if __name__ == '__main__':
    count = 1
    prefix_name = 'left'
    # img = cv2.imread('D:\\Graduate-Design\\Graduation-Project\\Gesture_Recognition\\handImg\\small.png')
    # cv2.imshow('hello', img)

    for i in range(1, 21):
        roi = cv2.imread(path + prefix_name + '_' + str(i) + '.png')
        while count > 20:
            rota_img = rotate(roi)
            cv2.imwrite(write_path + prefix_name + '_' + str(count) + '.png', rota_img)
            count += 1
            flip_img = cv2.flip(rota_img, 1)
            cv2.imwrite(write_path + prefix_name + '_' + str(count) + '.png', flip_img)
            count += 1
        print(prefix_name + '_' + str(i) + 'Done.')
