# -*- coding:utf-8 -*-
# タプルの基本的な操作
# タプル : tpl = (, ,...)
# リストと違って初期化したタプルはイミュータブル(不変)

tpl1 = (1, 2, 3, 4, 5)
tpl2 = "月", "火", "水", "木", "金"  # ()無しでも可
print(tpl1)
print(tpl2)

# 複数の変数にタプルの値を代入
# 用意する変数の数はタプルの要素数(それ以外だとエラー)
a, b, c, d, e = tpl1
print(a)
print(b)
print(c)
print(d)
print(e)
print()

# set型オブジェクトの操作
s = {"A", "B", "C"}
print(s)

# 重複があっても無視される
s = {"A", "B", "C", "A"}
print(s)
print()

# set型はイミュータブル
# これはエラー(リストはハッシュ化可能ではない)
# s = {'A', [1, 2, 3]}
# print(s)
# リストではなくタプルにする
s = {'A', (1, 2, 3)}
print(s)

# listからsetを作る set()
l = ["a", "b", "c", "d"]
s = set(l)
print(s)
print()

# setの要素追加
s = {1, 2, 3}
s.add(4)
print(s)
print()

# setの要素削除 remove() discard()
# removeは存在しないオブジェクトを指定すると`KeyError`が発生
s = {1, 2, 3, 4}
s.remove(4)
print(s) # {1, 2, 3}
# KeyError発生
# s.remove(99)
 
s.discard(99)
print(s) # {1, 2, 3}

# 変更不可のset frozenset
# 変更不可以外はsetと同じ
fs = frozenset(["a", "b", "c"]) 
print(fs)
print()

# 辞書の基本的な操作
# 辞書(連想配列、ハッシュ)はミュータブル
# キーと値のペアで管理
# 辞書 : dic = {key:val}

number = {"one":1, "two":2, "three":3}
print(number)
# Keyをインデックスとして値にアクセス
print(number["one"])    # キーを指定
# getメソッドから値にアクセス
print(number.get("one"))
print()

# リストを辞書にする dict()
product_list = [["コーヒー", "100円"], ["パン", "200円"], ["おにぎり", "150円"]]
product_dict = dict(product_list)
print(product_dict)
print(product_dict["コーヒー"]) # 100円
print(product_list[0][1])       # コーヒー：100円
