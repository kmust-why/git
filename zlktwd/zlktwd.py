#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: config.py
#time: 17-10-8 上午9:19

# flask的主文件

from flask import Flask,render_template,request,redirect,url_for,session,g
import config
from models import UserModel,QuestionModel,AnswerModel
from exts import db
from decorators import login_required
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object(config) # 导入配置文件
db.init_app(app)





@app.route('/')
@login_required
def index():
    context = {
        'questions': QuestionModel.query.order_by('-create_time').all()
    }
    return render_template('index.html',**context)

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = UserModel.query.filter(telephone==telephone,password==password).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'用户名或密码错误！'

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        # 获取信息
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 手机号码验证，如果被注册了，则不能注册
        user = UserModel.query.filter(telephone==telephone).first()
        if user:
            return u'该手机号码已经被注册了，请更换手机号码！'
        else:
            # 验证两次输入的密码是否相同
            if password1 != password2:
                return u'两次输入的密码不相同，请核对后再输入！'
            else:
                # 写入数据库
                user = UserModel(telephone=telephone,username=username,password=password2)
                db.session.add(user)
                db.session.commit()
                # 注册成功，跳转到登录页面
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))

@app.route('/question/',methods=['GET','POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = QuestionModel(title=title, content=content)

        question.author = g.user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<question_id>/')
def detail(question_id):
    question = QuestionModel.query.filter(QuestionModel.id == question_id).first()
    return render_template('detail.html',question=question)

@app.route('/comment/',methods=['POST'])
@login_required
def comment():
    question_id = request.form.get('question_id')
    print(type(question_id))
    content = request.form.get('content')
    answer = AnswerModel(content=content)

    answer.author = g.user
    question = QuestionModel.query.filter(QuestionModel.id == question_id).first()
    answer.question =question
    db.session.add(answer)
    db.session.commit()

    return redirect(url_for('detail',question_id=question_id))

@app.route('/search/')
def search():
    q = request.args.get('q')
    questions = QuestionModel.query.filter(or_(QuestionModel.title.contains(q),QuestionModel.content.contains(q))).order_by('-create_time')
    context = {
        'questions': questions
    }
    return render_template('index.html',**context)


@app.context_processor
def my_context_processor():
    if hasattr(g,'user'):
        return {'user':g.user}
    else:
        return {}

@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = UserModel.query.filter(UserModel.id == user_id).first()
        if user:
            g.user = user


if __name__ == '__main__':
    app.run()
