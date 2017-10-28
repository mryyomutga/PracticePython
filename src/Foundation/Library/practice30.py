# -*- coding: utf-8 -*-
from __future__ import print_function

# jsonのエンコード

import json

# dict型からjson文字列に変換
dict_data = {"items":[{"id":1, "name":"pen"}, {"id":2, "name":"apple"}, {"id":3, "name":"textbook"}], "status":"sell"}

# json文字列形式
json_str = json.dumps(dict_data)
print(json_str, "\n")

# インデントを付けてdump
json_str = json.dumps(dict_data, indent=2)
print(json_str, "\n")

# asciiエンコードしない
json_str = json.dumps(dict_data, indent=2, ensure_ascii=False)
print(json_str, "\n")

# ソートする場合
json_str = json.dumps(dict_data, indent=2, sort_keys=True)
print(json_str, "\n")

# jsonからdictに変換する
json_str = '{"items":[{"id":1, "name":"pen"}, {"id":2, "name":"apple"}, {"id":3, "name":"textbook"}], "status":"sell"}'
dict_data = json.loads(json_str)
print(type(dict_data))
print(dict_data, "\n")

# jsonファイルからdictヘ変換する
f = open("sample.json", "r")
dict_data = json.load(f)
print(type(dict_data))
print(dict_data, "\n")
