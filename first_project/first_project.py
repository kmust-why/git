#!/usr/bin/env python
# -*- coding:utf-8 -*-

print('aaa')
from flask import Flask,url_for,redirect,render_template
import config
from exts import db


print('bbb')

app = Flask(__name__)
print('ccc')
app.config.from_object(config)
db.init_app(app)
with app.app_context():
    db.create_all()

print('ddd')





db.create_all()
@app.route('/<is_login>/')
def index(is_login):
    # article1 = Article.query.filter(title='李四',content='hah',author_id=1)
    # article1 = Article(title='李四',content='hah',author_id=1)
    # db.session.add(article1)
    # db.session.commit()
    # user = User(username = '王无')
    # db.session.add(user)
    # db.session.commit()
    # article1 = Article(title='李四',content='hah')
    # db.session.add(article1)
    # db.session.commit()
    # result = Article.query.filter(Article.id == 2).all()
    # print(type(result))
    # article1 = result[0]
    # print(article1.title)
    if is_login == '1':
        context = {
                'username':u'王海云',
            'sex':u'男',
            'age':23
        }
        return render_template('index.html',context=context)
    else:
        return render_template('index.html')
    # c = 1/0
    # login_url = url_for('login')
    #return redirect(login_url)
    # print(url_for('article',id = 12))
    # print(url_for('my_list'))
    # return 'Hello World!'

@app.route('/article/<id>/')
def article(id):
    return 'the id is %s' %id

@app.route('/list/')
def my_list():
    books = [
        {
            'name':u'三国演义',
            'author':u'罗贯中',
            'price':100
        },
        {
            'name':u'三国演义1',
            'author':u'罗贯中1',
            'price':200
        },
        {
            'name':u'三国演义2',
            'author':u'罗贯中2',
            'price':300
        },
        {
            'name':u'三国演义3',
            'author':u'罗贯中3',
            'price':400
        }
    ]
    return render_template('list.html',books=books)

@app.route('/login/')
def login():
    return u'这是登陆页面'

@app.route('/question/<is_login>/')
def question(is_login):
    if is_login == '1':
        return 'question'
    else:
        return redirect(url_for('login'))


print('eee')

if __name__ == '__main__':
    app.run()
