# -*- coding: utf-8 -*-
# filter関数
# lambda式と組み合わせることで簡略化が可能
from __future__ import print_function

# 奇数を判定する関数
def is_odd(val):
    return (val % 2) == 1

data1 = [x for x in range(1, 12)]
# data1の要素をis_oddのフィルターにかける
data2 = filter(is_odd, data1)
print("{0}\n{1}\n{2}\n".format(data1, data2, list(data2)))

# lambda式と組み合わせる
print("lambda")
data1 = [x for x in range(1, 12)]
data2 = filter(lambda x : x % 2 == 1, data1)
print("{0}\n{1}\n{2}\n".format(data1, data2, list(data2)))
