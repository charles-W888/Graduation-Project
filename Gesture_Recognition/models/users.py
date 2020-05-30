# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/5 23:20
 @Author  : Charles
 @Project   : Gesture_Recognition
 @File    : users.py
 @Software: PyCharm
 """
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class User:
    def __init__(self):
        """
        创建数据库连接和数据表
        :return: null
        """
        self._db = QSqlDatabase.addDatabase("QSQLITE")

        # 创建数据库userlog.db,如果存在则打开，否则创建该数据库
        self._db.setDatabaseName('./userlog.db')
        self._db.open()
        self.__query = QSqlQuery()

    def createTable(self):
        sql = u"CREATE TABLE logUser (uname VARCHAR(20), passwd VARCHAR (20));"
        self.__query.exec_(sql)

    def user_register(self, username, passwd):
        """
        用户注册，直接添加信息即可
        :param username:   用户名
        :param passwd:   密码
        :return:   if insert successfully, return true; then return false
        """
        # INSERT INTO logUser (uname, passwd) VALUES(username, passwd);
        # sql = u"-- INSERT INTO logUser (uname, passwd) VALUES(" + username + ", " + passwd + ");"
        sql = u"INSERT INTO logUser (uname, passwd) VALUES(?, ?);"
        self.__query.prepare(sql)
        self.__query.addBindValue(username)
        self.__query.addBindValue(passwd)
        if self.__query.exec_():
            print('OKOKOKOK!!')
            return True
        return False

    def user_login(self, username, passwd):
        """
        判断登录用户信息
        :param username:  用户名
        :param passwd:   密码
        :return:   if username and password correct, return true; then return false
        """
        # SELECT * FROM logUser WHERE uname=username and passwd=passwd;
        sql = u"SELECT * FROM logUser WHERE uname=? and passwd=?;"
        self.__query.prepare(sql)
        self.__query.bindValue(0, username)
        self.__query.bindValue(1, passwd)
        # self.__query.exec()
        if self.__query.exec():
            print('OK')
            return True
        return False

    def closeDB(self):
        self._db.close()
