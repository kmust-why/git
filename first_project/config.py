#!/usr/bin/env python
# -*- coding:utf-8 -*-

DEBUG = True

# 数据库的配置
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '123456why'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo2'


SQLALCHEMY_DATABASE_URI= "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

#SQLALCHEMY_DATABASE_URI = False
SQLALCHEMY_TRACK_MODIFICATIONS = False