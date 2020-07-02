# Python--时间日期处理小结
# http://www.wklken.me/posts/2015/03/03/python-base-datetime.html

import time
import datetime
now = datetime.datetime.now()
print(now,'-----n')

print(time.localtime())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'---st')
print(datetime.datetime.now().date(),'---dt')
print(datetime.date.today()+datetime.timedelta(days=1))
print(datetime.date.today()+datetime.timedelta(days=-1),'-----0')
print(datetime.datetime.combine(datetime.date.today(),datetime.time.min),'---min')  #获取当天开始和结束时间(00:00:00 23:59:59)
print(datetime.datetime.combine(datetime.date.today(),datetime.time.max),'-----max')  #获取当天开始和结束时间(00:00:00 23:59:59)
today = datetime.date.today()
sunday = today + datetime.timedelta(6 - today.weekday())  # 获取本周/本月/上月最后一天


"""
1. datetime
>>> import datetime
>>> now = datetime.datetime.now()
>>> now
datetime.datetime(2015, 1, 12, 23, 9, 12, 946118)
>>> type(now)
<type 'datetime.datetime'>
2. timestamp
>>> import time
>>> time.time()
1421075455.568243
3. time tuple
>>> import time
>>> time.localtime()
time.struct_time(tm_year=2015, tm_mon=1, tm_mday=12, tm_hour=23, tm_min=10, tm_sec=30, tm_wday=0, tm_yday=12, tm_isdst=0)
4. string
>>> import datetime
>>> datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
'2015-01-12 23:13:08'
5. date
>>> import datetime
>>> datetime.datetime.now().date()
datetime.date(2015, 1, 12)
datetime基本操作
1. 获取当前datetime
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2015, 1, 12, 23, 26, 24, 475680)
2. 获取当天date
>>> datetime.date.today()
datetime.date(2015, 1, 12)
3. 获取明天/前N天
明天

>>> datetime.date.today() + datetime.timedelta(days=1)
datetime.date(2015, 1, 13)
三天前

>>> datetime.datetime.now()
datetime.datetime(2015, 1, 12, 23, 38, 55, 492226)
>>> datetime.datetime.now() - datetime.timedelta(days=3)
datetime.datetime(2015, 1, 9, 23, 38, 57, 59363)
4. 获取当天开始和结束时间(00:00:00 23:59:59)
>>> datetime.datetime.combine(datetime.date.today(), datetime.time.min)
datetime.datetime(2015, 1, 12, 0, 0)
>>> datetime.datetime.combine(datetime.date.today(), datetime.time.max)
datetime.datetime(2015, 1, 12, 23, 59, 59, 999999)
5. 获取两个datetime的时间差
>>> (datetime.datetime(2015,1,13,12,0,0) - datetime.datetime.now()).total_seconds()
44747.768075
6. 获取本周/本月/上月最后一天
本周

>>> today = datetime.date.today()
>>> today
datetime.date(2015, 1, 12)
>>> sunday = today + datetime.timedelta(6 - today.weekday())
>>> sunday
datetime.date(2015, 1, 18)
本月

>>> import calendar
>>> today = datetime.date.today()
>>> _, last_day_num = calendar.monthrange(today.year, today.month)
>>> last_day = datetime.date(today.year, today.month, last_day_num)
>>> last_day
datetime.date(2015, 1, 31)
获取上个月的最后一天(可能跨年)

>>> import datetime
>>> today = datetime.date.today()
>>> first = datetime.date(day=1, month=today.month, year=today.year)
>>> lastMonth = first - datetime.timedelta(days=1)
关系转换
几个关系之间的转化

Datetime Object / String / timestamp / time tuple

关系转换例子
datetime <=> string
datetime -> string

>>> import datetime
>>> datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
'2015-01-12 23:13:08'
string -> datetime

>>> import datetime
>>> datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S")
datetime.datetime(2014, 12, 31, 18, 20, 10)
datetime <=> timetuple
datetime -> timetuple

>>> import datetime
>>> datetime.datetime.now().timetuple()
time.struct_time(tm_year=2015, tm_mon=1, tm_mday=12, tm_hour=23, tm_min=17, tm_sec=59, tm_wday=0, tm_yday=12, tm_isdst=-1)
timetuple -> datetime

timetuple => timestamp => datetime [看后面datetime<=>timestamp]
datetime <=> date
datetime -> date

>>> import datetime
>>> datetime.datetime.now().date()
datetime.date(2015, 1, 12)
date -> datetime

>>> datetime.date.today()
datetime.date(2015, 1, 12)
>>> today = datetime.date.today()
>>> datetime.datetime.combine(today, datetime.time())
datetime.datetime(2015, 1, 12, 0, 0)
>>> datetime.datetime.combine(today, datetime.time.min)
datetime.datetime(2015, 1, 12, 0, 0)
datetime <=> timestamp
datetime -> timestamp

>>> now = datetime.datetime.now()
>>> timestamp = time.mktime(now.timetuple())
>>> timestamp
1421077403.0
timestamp -> datetime

>>> datetime.datetime.fromtimestamp(1421077403.0)
datetime.datetime(2015, 1, 12, 23, 43, 23)

"""








# http://www.wklken.me/posts/2015/03/03/python-base-datetime.html#datetime-date



