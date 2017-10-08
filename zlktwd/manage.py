#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: manage.py
#time: 17-10-8 上午9:33

# 用来存放相应的命令
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from zlktwd import app
from exts import db
from models import UserModel,QuestionModel,AnswerModel


manager = Manager(app)

# 绑定app和db
migrate = Migrate(app,db)

# 添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()