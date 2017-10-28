# -*- coding: utf-8 -*-
# zip関数
from __future__ import print_function

data1 = [x for x in range(1, 6)]
data2 = [chr(s) for s in range(97, 97+6)]   # アルファベットの文字列リスト

print(data1, data2)

# 複数のリストを同時にfor文で回す
for x, y in zip(data1, data2):
    print(x, y)

# 3つ以上で回す
data3 = {"a":1, "b":2, "c":3, "d":4, "e":5}

for x, y, (key, value) in zip(data1, data2, data3.items()):
    print(x, y, "  data3[{0}]:{1}".format(key, value))

# 長さが異なるリストで回す
data1 = [x for x in range(0, 3)]
data2 = [x for x in range(1, 5)]
data3 = [x for x in range(2, 7)]

# 最も短いリストに合わせる
for x, y, z in zip(data1, data2, data3):
    print(x, y, z)

# ループインデックスを取得する場合
for idx, (x, y, z) in enumerate(zip(data1, data2, data3)):
    print(idx, x, y, z)
