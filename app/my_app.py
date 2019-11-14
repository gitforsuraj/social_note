import os
import sqlite3
import datetime
import json
from flask import Flask, render_template, jsonify, request, g
from flask_materialize import Material  
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators, DateField, SelectField
from wtforms.validators import Required
from todo_item import TodoItem
from user import User
from firebase_admin import credentials, firestore, initialize_app
import helpers

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(THIS_FOLDER, 'database.db')

app = Flask(__name__)  
Material(app)  
app.config['SECRET_KEY'] = 'USE-YOUR-OWN-SECRET-KEY-DAMNIT'
app.config['RECAPTCHA_PUBLIC_KEY'] = 'TEST'

#mock data
todo_items = {'todo1':True, 'todo222':False,'just simple to do':True}
todos = [TodoItem('This is a mock todo that has not been completed yet',False, datetime.datetime.now())]
init = False

#mock data
ButtonPressed = 0

#mock data
currentUser = None


# straight from the wtforms docs:
class TelephoneForm(Form):
    country_code = IntegerField('Country Code', [validators.required()])
    area_code = IntegerField('Area Code/Exchange', [validators.required()])
    number = TextField('Number')

class ExampleForm(Form):
    field1 = TextField('Title', description='')
    # field2 = TextField('Second Field', description='This is field two.',
    #                    validators=[Required()])
    # hidden_field = HiddenField('You cannot see this', description='Nope')
    # recaptcha = RecaptchaField('A sample recaptcha field')
    # radio_field = RadioField('This is a radio field', choices=[
    #     ('head_radio', 'Head radio'),
    #     ('radio_76fm', "Radio '76 FM"),
    #     ('lips_106', 'Lips 106'),
    #     ('wctr', 'WCTR'),
    # ])
    # checkbox_field = BooleanField('This is a checkbox',
    #                               description='Checkboxes can be tricky.')

    # # subforms
    # mobile_phone = FormField(TelephoneForm)

    # # you can change the label as well
    # office_phone = FormField(TelephoneForm, label='Your office phone')

    # ff = FileField('Sample upload')

    submit_button = SubmitField('Create')


    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

#create a todo in database
def create_todo(todo:TodoItem):
    user_id = 'first_user'
    todo_tuple = (user_id, todo.title,todo.creation_date.strftime("%m/%d/%Y, %H:%M:%S"), 1 if todo.is_done else 0)
 
    query = ''' INSERT INTO todos(user_id,title,date,is_done)
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
              WHERE title = ?
              VALUES(?,?)'''
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

@app.route('/',methods=["GET", "POST"])  
def my_app():
    form = ExampleForm()   
    if form.field1.data != None:
        title = form.field1.data
        todo_item = TodoItem(title, False, datetime.datetime.now())
        create_todo(todo_item)
        print(form.field1.data)
    else:
        form.field1.description = ''
    global ButtonPressed
    ButtonPressed += 1
    """
        create() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """


    #get all todos from database
    print('before the for loop')
    todos.clear()
    for todo in query_db('select * from todos'):
        print(todo)
        todo_items[todo[1]] = False
        if todo[2] != '':
            temp_todo = TodoItem(todo[1], True if todo[3]==1 else False, datetime.datetime.strptime(todo[2],"%m/%d/%Y, %H:%M:%S"))
            print(temp_todo.is_done)
            todos.append(temp_todo)

    form.field1.data = ""
    return render_template('home.html', ButtonPressed = ButtonPressed,form = form, todo_items = todo_items, todos = todos, get_time_elapse = helpers.get_time_elapse)  

if __name__ == '__main__':  
    app.run(debug = True)  

@app.route('/background_process_test',method = ["GET","POST"])
def background_process_test():
    print("Hello there")
    # for(key,value in todo_items):
    #     value = False
    return "{'name':'J'}"

@app.route("/forward/")
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    print(forward_message)
    return 'nothing'
    #return render_template('index.html', forward_message=forward_message);