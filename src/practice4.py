# -*- coding:utf-8 -*-
# タプルの基本的な操作
# タプル : tpl = (, ,...)

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

# 辞書の基本的な操作
# 辞書(連想配列、ハッシュ)はミュータブル
# キーと値のペアで管理
# 辞書 : dic = {key:val}

number = {"one":1, "two":2, "three":3}
print(number)
print(number["one"])    # キーを指定
print()

# リストを辞書にする dict()
product_list = [["コーヒー", "100円"], ["パン", "200円"], ["おにぎり", "150円"]]
product_dict = dict(product_list)
print(product_dict)
print(product_dict["コーヒー"]) # 100円
print(product_list[0][1])       # コーヒー：100円
