#import pytest

from datetime import datetime
from todo_item import TodoItem

# @pytest.fixture(scope='module') 
# def new_todoitem():
#     todoitem = TodoItem('this is title',True, datetime(days=50,seconds=27,microseconds=10,milliseconds=29000,minutes=5,hours=8,weeks=2)) 
#     return todoitem

def test_new_todoitem():
    todoitem = TodoItem('this is title',True, datetime(year= 2019, month = 10,day= 29)) 
    assert todoitem.title == 'this is title' 
    assert todoitem.is_done == True
    assert todoitem.creation_date == datetime(year= 2019, month = 10,day= 29)