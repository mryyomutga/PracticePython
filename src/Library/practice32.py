# -*- coding: utf-8 -*-
# オブジェクトのコピー
from __future__ import print_function
import copy

# 単純なコピー
data1 = {"key1":100}
data2 = data1           # data2はdata1の参照がコピー

print(data1, data2)
del data2["key1"]

print(data1, data2, "\n")     # data1も削除される

# copyモジュールで浅いコピーをする
data1 = {"key1":100, "key2":[1, 2]}
data2 = copy.copy(data1)    # data1をコピーする

print(data1, data2)

del data2["key1"]
print(data1, data2)         # data1は削除されない

data2["key2"][0] = 100      # data2の"key2"の値を変更する
# オブジェクト内部の参照は同じなため、data1も書き換わる
print(data1, data2, "\n")

# 深いコピー(全く同じ内容の別のオブジェクトの生成)
data1 = {"key1":100, "key2":[1, 2]}
data2 = copy.deepcopy(data1)    # 深いコピーを行う(dict, list)

print(data1, data2)
data2["key2"][0] = 100
# オブジェクトの参照先のオブジェクトもコピーされている
print(data1, data2, "\n")

# 独自クラスのコピー
class sample(object):
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text

    # 自分自身と同じオブジェクトを生成する
    def __deepcopy__(self, text):
        new_obj = sample(self.text)
        return new_obj

data1 = {"key1":100, "key2":sample("data1_obj")}
data2 = copy.deepcopy(data1)

data2["key2"].text = "data2_obj"
# sampleクラスに__deepcopy__メソッドがない場合、出力結果が同じになる
print(data1, data2)
