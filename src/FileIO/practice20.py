# -*- coding: utf-8 -*-
# ファイル・ディレクトリの存在確認

import os
import shutil
path = "practice19.py"

if os.path.exists(path):
    print("指定したパスは存在します")

    if os.path.isfile(path):
        print("ファイル")
    elif os.path.isdir(path):
        print("ディレクトリ")
else:
    print("指定したパスは存在しません")
    quit()

# ファイルの削除
os.remove("sample2.txt")

# ディレクトリの作成・削除
os.mkdir("dir_1")               # 単一階層
os.makedirs("dir_2/dir_3")      # 複数階層

os.rmdir("dir_1")
os.removedirs("dir_2/dir_3")

os.mkdir("dir_1")

shutil.copy("sample.txt", "test.txt")   # 単一コピー
shutil.copytree("dir_1/", "dir_2/")     # ディレクトリ毎に再帰的コピー
