#import pytest

from datetime import datetime
from models import User

# @pytest.fixture(scope='module') 
# def new_todoitem():
#     todoitem = TodoItem('this is title',True, datetime(days=50,seconds=27,microseconds=10,milliseconds=29000,minutes=5,hours=8,weeks=2)) 
#     return todoitem

def test_new_user():
    user = User()
    user.create_user('user','passcode')
    assert user.user_name == 'user' 
    assert user.passcode == 'passcode'