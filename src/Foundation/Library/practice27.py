# -*- coding: utf-8 -*-
# 辞書型で順序を保つ
# 辞書型は順序が不定
# Python3.6でdictの実装が変わり、dictが省メモリになり、キーの順番が維持されるようになった

data_dict = {'apple': 60, 'orange': 80, 'banana': 100}
for key, val in data_dict.items():
    print(key, val)
print()

# 順序を保つためにOrderedDictを使用する
# collectionsモジュールのOrderedDictをimport
from collections import OrderedDict
data_dict = OrderedDict()
data_dict["apple"] = 60
data_dict["orange"] = 80
data_dict["banana"] = 100

for key, val in data_dict.items():
    print(key, val)
