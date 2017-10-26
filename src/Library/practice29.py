# -*- coding: utf-8 -*-
# date, time

# date
from datetime import datetime, date, time, timedelta
# 年・月・日を指定
d = date(2017, 1, 2)
print(d)
print()

# 文字列からdateへの変換
dt_str = "2017-10-26"
# dateにはstrptimeに相当するものがない
dt_obj = datetime.strptime(dt_str, "%Y-%m-%d")

d = dt_obj.date()   # datetime型からdate型に変換
print(d)
print()

# 現在日時の取得
dt_obj_now = datetime.now() # datetimeから取得
d = dt_obj_now.date()       # date型変換
print(d)
print()

# 日数の計算
d1 = date(2016, 11, 25)
d2 = datetime.now().date()
delta = d2- d1
print(delta)
print()

# time
# 時・分・秒を指定
t = time(13, 0, 0)
print(t)
print()

# 文字列からtimeへの変換
dt_str = "13:35:24"
dt_obj = datetime.strptime(dt_str, "%H:%M:%S")
t = dt_obj.time()
print(t)
