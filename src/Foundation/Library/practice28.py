# -*- coding: utf-8 -*-
# 日付と時間
# datetimeモジュール

from datetime import datetime

# datetimeオブジェクト生成
# コンストラクタに年・月・日・時間・分・秒・マイクロ秒を指定
dt_obj = datetime(2018, 1, 2, 12, 0, 0, 000000)
print(dt_obj)
print()

# 現在日時の取得
dt_obj_now = datetime.now() # 現在日時を取得
print(dt_obj_now)
print()

# 日付・時刻要素の取得
dt_obj = datetime(2017, 10, 26, 12, 30, 0, 000000)
print(dt_obj)
print(dt_obj.year)          # 年
print(dt_obj.month)         # 月
print(dt_obj.day)           # 日
print(dt_obj.hour)          # 時
print(dt_obj.minute)        # 分
print(dt_obj.second)        # 秒
print(dt_obj.microsecond)   # マイクロ秒
print()

# 文字列からdatetimeへの変換
dt_str = "2017-10-26 12:30:05"
dt_obj = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
print(dt_obj)
print(type(dt_obj))
print()

# datetimeから文字列への変換
dt_obj_now = datetime.now()
dt_str = dt_obj.strftime("%Y/%m/%d %H:%M:%S")
print(dt_str)
print()

# datetiemの加減算
from datetime import datetime, timedelta
# 基準の日時
dt_obj1 = datetime.now()
print(dt_obj1)

delta = timedelta(days=1)   # 1日分の間隔

# 1日後
dt_obj2 = dt_obj1 + delta
print(dt_obj2)

# 1日前
dt_obj3 = dt_obj1 - delta
print(dt_obj3)

dt_obj1 = datetime(2018, 10, 20, 12, 45, 20, 000000)
dt_obj2 = datetime.now()

# 日付の間隔
delta = dt_obj1 - dt_obj2
print(delta)

