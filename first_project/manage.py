#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask_script import Manager
from first_project import app
from db_scripts import db_manager

manager = Manager(app)

@manager.command
def runserver():
    print('service is running....')

manager.add_command('db',db_manager)


if __name__ == '__main__':
    manager.run()
