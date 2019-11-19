import os
import sqlite3
import datetime
import json
from flask import render_template, flash, redirect, url_for, jsonify, request, g, Flask
from app import app
from app import db
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.models import User
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse
from todo_item import TodoItem
from flask import Flask, render_template, jsonify, request, g
from flask_materialize import Material  
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators, DateField, SelectField
from wtforms.validators import Required
import helpers

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
key_json_file_path = os.path.join(THIS_FOLDER, 'key.json')
DATABASE = os.path.join(THIS_FOLDER, 'database.db')

#mock data
todo_items = {'todo1':True, 'todo222':False,'just simple to do':True}
todos = [TodoItem('This is a mock todo that has not been completed yet',False, datetime.datetime.now())]

# straight from the wtforms docs:
class TelephoneForm(Form):
    country_code = IntegerField('Country Code', [validators.required()])
    area_code = IntegerField('Area Code/Exchange', [validators.required()])
    number = TextField('Number')

class ExampleForm(Form):
    field1 = TextField('Title', description='')

    submit_button = SubmitField('Create')


    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), username = 'todos', one=False):
    try:
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

    except:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS """+current_user.username+""" (
                                        user_id text NOT NULL,
                                        title text NOT NULL,
                                        date text NOT NULL,
                                        is_done integer default 0
                                    )"""
        query = ''' INSERT INTO ''' + username + '''(user_id,title,date,is_done)
              VALUES(?,?,?,?) '''
        db = get_db()
        #db.execute("PRAGMA busy_timeout = 30000")
        cur = db.execute(sql_create_table)
        db.commit()
        cur.close()

        # #create the first todo for first-time user
        # args = (username, 'This is your first todo', datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),0)
        # cur = db.execute(query, args)
        # #cur.commit()

        query = 'select * from '+current_user.username
        cur = get_db().execute(query, ())
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

def query_db_by_username(username,query, args=(), one=False):
    cur = get_db().execute("SELECT name FROM sqlite_master WHERE type='table' AND name= ? ", ('todos',))
    print("printing cur")
    print(cur)
    rv = cur.fetchall()
    print("printing rv")
    print(rv)
    cur.close()
    return (rv[0] if rv else None) if one else rv

#create a todo in database
def create_todo(todo:TodoItem):
    user_id = current_user.username
    todo_tuple = (user_id, todo.title,todo.creation_date.strftime("%m/%d/%Y, %H:%M:%S"), 1 if todo.is_done else 0)
 
    query = ''' INSERT INTO '''+ current_user.username+'''(user_id,title,date,is_done)
              VALUES(?,?,?,?) '''
    db = get_db()
    cur = db.cursor()
    cur.execute(query, todo_tuple)
    db.commit()
    #db.close()
    return 0

#update a todo in database
def update_todo(title:str, is_done:bool):
    user_id = 'first_user'
    todo_tuple = (is_done, title)
 
    query = ''' UPDATE todos
                SET is_done = ?
                WHERE title = ?'''
    db = get_db()
    cur = db.cursor()
    cur.execute(query, todo_tuple)
    db.commit()
    #db.close()
    return 0



@app.route('/postmethod',methods = ['POST'])
def get_post_javascript_data():
    print(request.form['data'])
    data = json.loads(request.form['data'])

    print(data)
    print('checking post data')

    todo_items[data['title']] = False if data['val'] == 0 else True

    update_todo(data['title'], False if data['val'] == 0 else True)

    return ''


@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
@login_required
def index():
    form = ExampleForm()   
    if form.field1.data != None:
        title = form.field1.data
        todo_item = TodoItem(title, False, datetime.datetime.now())
        create_todo(todo_item)
        print(form.field1.data)
    else:
        form.field1.description = ''

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]


    

    #get all todos from database
    print('before the for loop')
    todos.clear()
    username = current_user.username
    print(current_user.username)
    for todo in query_db('select * from {username}'):
        print(todo)
        todo_items[todo[1]] = False
        if todo[2] != '':
            temp_todo = TodoItem(todo[1], True if todo[3]==1 else False, datetime.datetime.strptime(todo[2],"%m/%d/%Y, %H:%M:%S"))
            print(temp_todo.is_done)
            todos.append(temp_todo)

    form.field1.data = ""

    return render_template('home.html', title='Home', posts=posts, form = form, todo_items = todo_items, todos = todos, get_time_elapse = helpers.get_time_elapse)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        # look at first result first()
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # return to page before user got asked to login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)