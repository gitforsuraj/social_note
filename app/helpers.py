import datetime
import typing

def get_time_elapse(d:datetime.datetime):
    now = datetime.datetime.now()
    if d == None:
        d = datetime.datetime.now()

    if now.year - d.year >= 0 :
        return str(now.year - d.year) + ' years ago'
    elif now.month - d.month >= 0:
        return str(now.month - d.month) + ' months ago'
    elif now.day - d.day >= 0:
        return str(now.day - d.day) + ' days ago'
    elif now.hour - d.hour >= 0:
        return str(now.hour - d.hour) + ' hours ago'
    elif now.minute - d.minute >= 0:
        return str(now.minute - d.minute) + ' mintues ago'
    else:
        return 'Created just now'