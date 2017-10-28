# -*- coding:utf-8 -*-
# id関数
# オブジェクトには固有のIDが割り振られる

num = 10
text = "aaaa"
dic = {"key":100}

print(id(num))
print(id(text))
print(id(dic))
print()

# 文字列型の同一性
text1 = "aaa"
text2 = text1
text3 = text1 + "bbb"

print(id(text1))
print(id(text2))
print(id(text3))

text1 = "bbb"
print(id(text1))