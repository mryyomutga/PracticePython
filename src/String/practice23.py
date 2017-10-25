# -*- coding: utf-8 -*-
# 文字列のフォーマット
# printf形式
# タプルで指定
print("タプル")
text = "There are %s, %s and %s."
f_text = text % ("apples", "bananas", "oranges")
print(f_text,"\n")

# 辞書で指定
print("辞書")
text = "There are %(first)s, %(second)s and %(third)s."
f_text = text % {"first":"apples", "second":"bananas", "third":"oranges"}
print(f_text, "\n")

# formatメソッド
print("formatメソッド")
text = "There are {0}, {1} and {2}."
f_text = text.format("apples", "bananas", "oranges")
print(f_text, "\n")
