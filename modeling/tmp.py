# -*- coding: utf-8 -*- 

# @Time : 2021-03-18 13:49 
# @Author : hht 
# @File : tmp.py
# @Desc:

import datetime,time
from datetime import datetime
from datetime import timedelta
def get_delta_date_string(delta: int):
    today_str = datetime.today().strftime('%Y%m%d')
    if delta < 0:
        delta = -delta
        return (datetime.strptime(today_str, '%Y%m%d') - \
                timedelta(days=delta)).strftime('%Y%m%d')
    else:
        return (datetime.strptime(today_str, '%Y%m%d') + \
                timedelta(days=delta)).strftime('%Y%m%d')
print("hello modeling")

print(type(get_delta_date_string(10)))