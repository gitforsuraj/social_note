import datetime
from typing import List

class TodoItem:
    title = ''
    is_done = False
    creation_date = None

    def __init__(self):
        creation_date = datetime.now()

    def __init__(self, title, is_done, creation_date):
        self.title = title
        self.is_done = is_done
        self.creation_date = creation_date
