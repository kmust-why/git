#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_script import Manager

db_manager = Manager()

@db_manager.command
def init():
    print(u'数据库初始化完成')

@db_manager.command
def imgrate():
    print(u'数据库迁移完成')
