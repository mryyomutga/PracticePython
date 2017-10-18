# -*- coding:utf-8 -*-
# リストの操作
# リスト : list = [, , ...]
# 2017/10/18 削除・挿入・ソートの追加

fruits = ["apple", "orange", "banana"]
print(fruits[0])    # apple
print(fruits[1])    # orange
print(fruits[2])    # banana
print(fruits)       # リストの内容
print()

# 空のリストの作成
emp = list()
print(emp)
print()

# 文字列をリストにする
greet = list("Hello")
print(greet)
print()

# splitを使ってリストにする
s = "こんにちは。文字列に関するプログラムです。Python3で実行できます。<<end"
sentencs = s.split("。")
print(sentencs)
print(sentencs[0])
print(sentencs[1])
print(sentencs[2])
print(sentencs[3])
print()

# リストの中にリストを格納する
jpn = [["北陸", "石川", "富山", "福井"], ["関東", "東京", "千葉", "神奈川", "茨城"]]
print(jpn)
print(jpn[0])       # 北陸～
print(jpn[1])       # 関東～
print(jpn[0][0])    # 北陸
print(jpn[0][1])    # 石川
print(jpn[0][2])    # 富山
print(jpn[0][3])    # 福井
print()

# 要素の変更
car = ["車", "タイヤ", "エンジン"]
print(car)
car[0] = "自動車"
print(car)
print()

# リストをスライス
foods = ["ケーキ", "チョコレート", "クッキー", "飴", "クラッカー"]
print(foods)
print(foods[0:2])   # ['ケーキ', 'チョコレート']
print(foods[1:3])   # ['チョコレート', 'クッキー']
print(foods[0:5:2]) # ['ケーキ', 'クッキー', 'クラッカー']
print(foods[::-1])  # 要素を反転
print()

# 要素の追加 append()
car.append("ライト")
print(car)
print(car[3])
print()

# リストの結合 extend()
sub1 = ["数学", "国語", "英語"]
sub2 = ["理科", "社会"]
print(sub1)
print(sub2)
sub1.extend(sub2)   # sub1の末尾にsub2の要素を追加
print(sub1)
print()

# 要素の削除 del
sub1 = ["数学", "国語", "英語"]
print(sub1)
# 指定した場所の要素を削除
# 先頭、、末尾は 0, -1
del sub1[1]
print(sub1)
print()

# remove
l = ["a", "b", "c", "d", "c"]
l.remove("a")   # aを削除
print(l)
l.remove("c")   # 先頭のcを削除
print(l)
print()

# pop
# 引数なしの場合、末尾のデータを取り出す
l = ["a", "b", "c", "d", "c"]
val = l.pop(2)  # 2番目のデータを取り出して削除
print(l)
print(val)
print()

# 要素の挿入 insert()
# 先頭に挿入
sub1.insert(0, "体育")
print(sub1)

# 2番目に挿入
sub1.insert(2, "美術")
print(sub1)

# 末尾に挿入
sub1.insert(-1, "物理")
print(sub1)
print()

# リストのソート sorted()
# 元のリストを変更しない場合
# 昇順にソート
l = ["c", "f", "a", "e", "b"]
print(sorted(l))

# 逆順にソート
print(sorted(l, reverse=True))
print("元のリスト : ", l)

# 大文字・小文字の区別
l = ["Ac", "bA", "aB", "bc"]

# 区別あり
print(sorted(l))

# 区別なし
print(sorted(l, key=str.lower))
print()

# リストを変更する場合 sort()
# 昇順にソート
l = ["c", "f", "a", "e", "b"]
l.sort()
print(l)

# 逆順にソート
l = ["c", "f", "a", "e", "b"]
l.sort(reverse=True)
print(l)

# 大文字・小文字の区別なし
l = ["Ac", "bA", "aB", "bc"]
l.sort(key=str.lower)
print(l)
