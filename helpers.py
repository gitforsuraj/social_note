import datetime
import typing

def get_time_elapse(d:datetime.datetime):
    now = datetime.datetime.now()
    if d == None:
        d = datetime.datetime.now()

    if now.year - d.year > 0 :
        return str(now.year - d.year) + ' year' + 's' if now.year - d.year > 1 else '' + ' ago'
    elif now.month - d.month > 0:
        return str(now.month - d.month) + ' month' + 's' if now.month - d.month > 1 else '' +' ago'
    elif now.day - d.day > 0:
        return str(now.day - d.day) + ' day' + 's' if now.day - d.day > 1 else '' +'ago'
    elif now.minute - d.minute > 60:
        return str(now.hour - d.hour) + ' hour' + 's' if now.hour - d.hour > 1 else '' + 'ago'
    elif now.minute - d.minute >0:
        return str(now.minute - d.minute) + ' mintue' + 's' if now.minute - d.minute > 1 else '' +'ago'
    else:
        return ' just now'