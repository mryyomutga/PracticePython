# -*- coding: utf-8 -*-
# 外部モジュールのimport
import math
print(math.pi)

# mathモジュールのpiだけを使用する場合
# math.を付けずに使用できる
from math import pi
print(pi)

# asで別名を付けて使用
import numpy
x = numpy.random.rand(50)
y = numpy.random.rand(50)
print(x, y)

# numpyモジュールをnpで使用できる
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)
print(x, y)

# モジュールと同名のクラス
import datetime
# datetimeモジュールにはdatetimeクラスが存在する
dt_obj = datetime.datetime(2017, 10, 25)
print(dt_obj)

# fromを使って書き換える
from datetime import datetime
dt_obj = datetime(2017, 10, 25)
print(dt_obj)
