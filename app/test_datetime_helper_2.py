import datetime
import helpers as helper

def test_datetime_helper_2():
    date1 = datetime.datetime.now()
    date2 = datetime.datetime(2017,1,1)
    
    assert helper.is_greater_than_24_hours(date1) == False
    assert helper.is_greater_than_24_hours(date2) == True

