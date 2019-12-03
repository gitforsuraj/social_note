import datetime
import helpers as helper

def test_datetime_helper():
    date1 = datetime.datetime(2018,1,1)
    date2 = datetime.datetime(2017,1,1)
    
    assert helper.get_time_elapse(date1) == '1 year ago'
    assert helper.get_time_elapse(date2) == '2 years ago'

