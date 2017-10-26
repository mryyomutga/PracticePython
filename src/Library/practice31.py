# -*- coding: utf-8 -*-
# CSVファイルの操作
from __future__ import print_function

import csv
with open("data.csv", "r") as f:
    reader = csv.reader(f)      # readerオブジェクトの生成
    print(type(reader))
    i = 1
    for row in reader:
        print("row {0}".format(i))
        print(row)
        # list型オブジェクトのためアクセス可能
        tmp = row[0]
        row[0] = row[-1]
        row[-1] = tmp
        print(row, "\n")
        i += 1

# ヘッダーを読み飛ばす
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(type(reader))
    for row in reader:
        print(row)
print()

# TSVファイルの読み出し
# 区切り文字を指定する
with open("data.tsv", "r") as f:
    reader = csv.reader(f, delimiter="\t")  # delimiterを指定する
    for row in reader:
        print(row)
print()

# CSVファイルの書き込み
list_data = [["a", "b", "c"], [1, 2, 3], [4, 5, 6]]
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list_data) # 行ごとに要素を書き込む
