# -*- coding: utf-8 -*-
# ファイル入出力
# open("ファイルパス", "モード")

f = open("sample.txt", "r")     # ファイルを開く
text = f.read()                 # ファイル読み込み
print(text)
f.close()                       # ファイルを閉じる

f = open("sample2.txt", "w")
f.write("sample text 2")
f.close()

# ファイルの読み書き
f = open("sample.txt", "r+")
text = f.read()
print(text)
f.write("append\n")
f.close()

# with文
# close処理が自動的に呼び出される
with open("sample.txt", "r+") as f:
    text = f.read()
    print(text)
    f.write("append2")
