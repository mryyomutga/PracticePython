# -*- coding: utf-8 -*-
# map関数
# lambda式と組み合わせるとさらに簡略化が可能
from __future__ import print_function

# 引数の値を2倍にする関数
def calc_double(val):
    return val * 2

x = 3
y = calc_double(x)
print(x, y)

data1 = [x for x in range(1, 100, 11)]
# calc_doubleでdata1の全ての要素を2倍にする
# data2はmapオブジェクトが格納されるため、appendなどできない
data2 = map(calc_double, data1)
print("{0}\n{1}\n".format(data1, data2))

# mapオブジェクトからリスト型へ変換する
print("convert list")
data2 = list(map(calc_double, data1))
print("{0}\n{1}\n".format(data1, data2))

# data2に要素をappend
print("append")
data2.append(1000)
print(data2, "\n")

# for文を使用する場合
print("for")
data2 = list()
for val in data1:
    data2.append(calc_double(val))
print(data2, "\n")


# lambda式を使う
print("lambda")
data1 = [x for x in range(0, 5)]
data2 = list(map(lambda x: x * 2, data1))
print("{0}\n{1}".format(data1, data2))
