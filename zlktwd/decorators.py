#encoding: utf-8

# 装饰器实质上是一个函数
# 装饰器的两个特点：
# 1.参数是一个函数
# 2.返回值也是一个函数
from functools import wraps
from  flask import session,redirect,url_for

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper

