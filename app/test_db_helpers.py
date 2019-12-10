import os
import sqlite3
import datetime
import json
from datetime import datetime
from todo_item import TodoItem

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
key_json_file_path = os.path.join(THIS_FOLDER, 'key.json')
DATABASE = os.path.join(THIS_FOLDER, 'database.db')

conn = sqlite3.connect(DATABASE)


# def get_db():
#     # db = getattr(g, '_database', None)
#     # if db is None:
#     conn = sqlite3.connect(DATABASE)

#     return conn

def check_table_exists(table_name):
    # conn = sqlite3.connect('mysqlite.db')
    # c = conn.cursor()

    sql_delete_table = ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=' '''+table_name+''' ' '''

    c = conn.cursor()
    c.execute(sql_delete_table)
    #db.execute("PRAGMA busy_timeout = 30000")
    #cur = db.execute(sql_delete_table)
    #c = db.cursor()
    conn.commit()

    
			
    #get the count of tables with the name
    #c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=' '''+table_name+''' ' ''')

    #if the count is 1, then table exists
    if c.fetchone()[0]==1: 
        
        #cur.close()
        return True
    else:
        
        return False

def create_todo(todo:TodoItem):
    user_id = 'test_table'
    todo_tuple = (user_id, todo.title,todo.creation_date.strftime("%m/%d/%Y, %H:%M:%S"), 1 if todo.is_done else 0)
 
    query = ''' INSERT INTO '''+ user_id +'''(user_id,title,date,is_done)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(query, todo_tuple)
    conn.commit()
    #db.close()
    return 0

def query_db(query, args=(), username = 'todos', one=False):
    try:
        c = conn.cursor()
        c.execute(query, args)
        rv = c.fetchall()
        #cur.close()
        return (rv[0] if rv else None) if one else rv

    except:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS """+ 'test_table'+""" (
                                        user_id text NOT NULL,
                                        title text NOT NULL,
                                        date text NOT NULL,
                                        is_done integer default 0
                                    )"""
        c = conn.cursor()
        #db.execute("PRAGMA busy_timeout = 30000")
        c.execute(sql_create_table)
        conn.commit()
        #cur.close()

        # #create the first todo for first-time user
        # args = (username, 'This is your first todo', datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),0)
        # cur = db.execute(query, args)
        # #cur.commit()

        query = 'select * from test_table'
        c.execute(query, ())
        conn.commit()
        rv = c.fetchall()
        #cur.close()
        return (rv[0] if rv else None) if one else rv

def delete_todo(title:str):
    user_id = 'test_table'
    query = '''DELETE FROM '''  + user_id +''' WHERE title=?'''
    query_tuple = (title,)
    
    cur = conn.cursor()
    cur.execute(query, query_tuple)
    conn.commit()

def delete_table(table_name):
    query = '''DROP TABLE IF EXISTS '''+ table_name
    cur = conn.cursor()
    #db.execute("PRAGMA busy_timeout = 30000")
    cur.execute(query)
    conn.commit()
    #cur.close()


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