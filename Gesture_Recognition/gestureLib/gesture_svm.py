# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/10 13:49
 @Author  : Charles
 @Project   : Gesture_Recognition
 @File    : gesture_svm.py
 @Software: PyCharm
 """
import os
import numpy as np
# from sklearn.externals import joblib
# import joblib
from sklearn.externals import joblib
from functools import reduce
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt


model_path = '../training_model'
feature_path = 'feature'

class ClassifierSVM:
    def __init__(self):
        pass

    def txt2Vector(self, filename, max):
        """
        将特征文件转成一维矩阵存储
        :param filename:  文件名
        :param max:
        :return:
        """
        count = 0
        vec = np.zeros((1, max))  # 1行max列的矩阵，初始全为0
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            for line in lines:
                _, fea = line.split(':')
                vec[0, count] = fea
                count += 1
            fr.close()

    def tran_SVM(self, max):
        svc = SVC()
        parameters = {'kernel': ('linear', 'rbf'),
                      'C': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
                      'gamma': [0.00001, 0.0001, 0.001, 0.1, 1, 10, 100, 1000]}  # 预设置一些参数值
        hwLabels = []  # 存放类别标签
        trainingFileList = os.listdir(feature_path)
        m = len(trainingFileList)
        trainingMat = np.zeros((m, max))
        for i in range(m):
            fileNameStr = trainingFileList[i]
            classNumber = int(fileNameStr.split('_')[0])
            hwLabels.append(classNumber)
            trainingMat[i, :] = ClassifierSVM.txt2Vector(feature_path + fileNameStr, max)  # 将训练集改为矩阵格式
        print("数据加载完成")
        clf = GridSearchCV(svc, parameters, cv=5, n_jobs=8)  # 网格搜索法，设置5-折交叉验证
        clf.fit(trainingMat, hwLabels)
        print(clf.return_train_score)
        print(clf.best_params_)  # 打印出最好的结果
        best_model = clf.best_estimator_
        print("SVM Model save...")
        save_path = model_path + "svm_efd_" + "train_model.m"
        joblib.dump(best_model, save_path)  # 保存最好的模型

    def test_fd(self, fd_test):
        clf = joblib.load("D:\\Graduate-Design\\Graduation-Project\\Gesture_Recognition\\training_model\\svm_train_model.m")
        test_svm = clf.predict(fd_test)
        return test_svm


# if __name__ == '__main__':
#     cs = ClassifierSVM()
#     cs.txt2Vector(feature_path, 500)
