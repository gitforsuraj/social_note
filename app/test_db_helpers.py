import os
import sqlite3
import datetime
import json
from datetime import datetime
from todo_item import TodoItem

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
key_json_file_path = os.path.join(THIS_FOLDER, 'key.json')
DATABASE = os.path.join(THIS_FOLDER, 'database.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = sqlite3.connect(DATABASE)
    return db

def check_table_exists(table_name):
    # conn = sqlite3.connect('mysqlite.db')
    # c = conn.cursor()

    sql_delete_table = ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=' '''+table_name+''' ' '''
    db = get_db()
    #db.execute("PRAGMA busy_timeout = 30000")
    cur = db.execute(sql_delete_table)
    #c = db.cursor()
    

    
			
    #get the count of tables with the name
    #c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=' '''+table_name+''' ' ''')

    #if the count is 1, then table exists
    if db.fetchone()[0]==1: 
        db.commit()
        cur.close()
        return True
    else:
        db.commit()
        cur.close()
        return False

def create_todo(todo:TodoItem):
    user_id = 'test_table'
    todo_tuple = (user_id, todo.title,todo.creation_date.strftime("%m/%d/%Y, %H:%M:%S"), 1 if todo.is_done else 0)
 
    query = ''' INSERT INTO '''+ current_user.username+'''(user_id,title,date,is_done)
              VALUES(?,?,?,?) '''
    db = get_db()
    cur = db.cursor()
    cur.execute(query, todo_tuple)
    db.commit()
    #db.close()
    return 0

def query_db(query, args=(), username = 'todos', one=False):
    try:
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

    except:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS """+ 'test_table'+""" (
                                        user_id text NOT NULL,
                                        title text NOT NULL,
                                        date text NOT NULL,
                                        is_done integer default 0
                                    )"""
        db = get_db()
        #db.execute("PRAGMA busy_timeout = 30000")
        cur = db.execute(sql_create_table)
        db.commit()
        cur.close()

        # #create the first todo for first-time user
        # args = (username, 'This is your first todo', datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),0)
        # cur = db.execute(query, args)
        # #cur.commit()

        query = 'select * from test_table'
        cur = get_db().execute(query, ())
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

def delete_todo(title:str):
    user_id = 'test_table'
    query = '''DELETE FROM '''  + user_id +''' WHERE title=?'''
    query_tuple = (title,)
    db = get_db()
    cur = db.cursor()
    cur.execute(query, query_tuple)
    db.commit()

def delete_table(table_name):
    query = '''DROP TABLE IF EXISTS '''+ table_name
    db = get_db()
    #db.execute("PRAGMA busy_timeout = 30000")
    cur = db.execute(query)
    db.commit()
    cur.close()


def test_db_helpers():
    table_name = 'test_table'
    assert check_table_exists(table_name) == False

    #testing query function(new table when if not exist)
    query_db('select * from {username}')
    assert check_table_exists(table_name) == True

    #testing insert function
    todoitem = TodoItem('this is title',True, datetime(year= 2019, month = 10,day= 29)) 
    create_todo(todoitem)

    #testing query function(get all rows from a table if exist)
    todos = []
    for todo in query_db('select * from {username}'):
        print(todo)
        
        if todo[2] != '':
            temp_todo = TodoItem(todo[1], True if todo[3]==1 else False, datetime.datetime.strptime(todo[2],"%m/%d/%Y, %H:%M:%S"))
            print(temp_todo.is_done)
            todos.append(temp_todo)
    assert todos[0].title == 'this is title'

    #testing delete row function
    delete_todo('this is title')
    assert len(query_db('select * from {username}')) == 0


    #testing delete table function
    delete_table(table_name)
    assert check_table_exists(table_name) == False