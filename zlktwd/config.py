#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: config.py
#time: 17-10-8 上午9:19

import os

# flask的配置文件
DEBUG = True # 开启调式功能
SECRET_KEY = os.urandom(24) # 配合使用

# mysql数据库的配置
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '123456why'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlktwd'


SQLALCHEMY_DATABASE_URI= "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False