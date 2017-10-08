#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: models.py
#time: 17-10-8 上午9:32

from exts import db
import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    telephone = db.Column(db.String(11),nullable=False)
    password = db.Column(db.String(100),nullable=False)

    def __init__(self,*args,**kwargs):
        password = kwargs.pop('password')
        username = kwargs.pop('username')
        telephone = kwargs.pop('telephone')
        self.password = generate_password_hash(password)
        self.username = username
        self.telephone = telephone

    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        return result


class QuestionModel(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    author = db.relationship('UserModel',backref=db.backref('questions'))


class AnswerModel(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.datetime.now)
    question_id = db.Column(db.Integer,db.ForeignKey('questions.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    question = db.relationship('QuestionModel',backref=db.backref('answers',order_by=create_time.desc()))
    author = db.relationship('UserModel',backref='answers')