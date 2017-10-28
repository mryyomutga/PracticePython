# -*- coding: utf-8 -*-
# reduce関数
from __future__ import print_function

from functools import reduce

# 引数の和を計算する関数
def add(arg1, arg2):
    return arg1 + arg2

# add関数を用いて前回の計算結果を引数にとって累積的に計算する
# 第1引数は引数2つもつ関数を指定
x = reduce(add, [x for x in range(1, 5)])
print(x)

# lambda式と組み合わせる
print("lambda")
x = reduce(lambda x, y: x + y, [x for x in range(1, 5)])
print(x)
