# -*- coding:utf-8 -*-
# for文

# range()を使うと指定回数だけ繰り返す
for i in range(5):
    print(i)
print()

# 初期値・限界・増分を設定
for i in range(1, 10, 2):
    print(i)
print()

# データを与えて回すことも可能
text = "ABCDEFG"

for s in text:
    print(s)
print()

# リストと組み合わせる
list = ["red", "green", "blue"]
print("List")
for c in list:
    print(c)
print()

# 辞書型と組み合わせる
dic = {"リンゴ":"apple", "オレンジ":"orange", "バナナ":"banana"}

# Keyのループ
print("Loop : Key")
for key in dic:
    print(key, dic[key])
print()

# Valueのループ
print("Loop : Value")
for val in dic.values():
    print(val)
print()

# KeyとValueのループ
print("Loop : Key, Value")
for key, value in dic.items():
    print(key, value)
print()

# ループインデックスの取得 enumerate()
print("Get Loop index")
# リスト
print("List")
for i, value in enumerate(list):
    print(i, value)
print()

# 辞書型
print("Dictionary")
for i, value in enumerate(dic):
    print(i, value)
print()

for i, (key, value) in enumerate(dic.items()):
    print(i, key, value)
print()

# for-else文
# elseブロック内の処理はループ処理終了時に必ず実行される
data_list = []
for data in data_list:
    print(data)
else:
    print("Finished loop")
print()

data_list = [1, 2, 3]
for data in data_list:
    print(data)
    if data > 1:
        break
else:
    print("Finished Loop")
print()