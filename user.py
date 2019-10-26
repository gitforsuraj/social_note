from todo_item import TodoItem
from typing import List

class User:
    user_name = ''
    user_email = ''
    todo_items = List[TodoItem]
    
    

    def __init__(self):
        user_name = ''
        user_email = ''

    def __init__(self, user_name:str, user_email:str, todo_items:List[TodoItem]):
        self.title = title
        self.is_done = is_done
        self.todo_items = todo_items