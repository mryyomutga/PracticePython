# -*- coding: utf-8 -*-
# mod1.py/mod2.py/mod3.pyの実行スクリプト
# 単一モジュールのimport
# 同じディレクトリ内にモジュールを作成する

import mod1     # mod1.pyモジュールのimport

# パッケージ化したモジュールのimport
# mypkgディレクトリ配下のモジュールのimport
from mypkg import mod2, mod3

mod1.func1()    # mod1のfunc1関数が実行される
mod2.func2()    # mod2のfunc1関数が実行される
mod3.MyClass().func3()  # mod3のMyClassクラスのfunc3関数が実行
print()

# __init__.pyに
# from . import mod2
# from . import mod3
# の記述があるとき

import mypkg

mypkg.mod2.func2()
mypkg.mod3.MyClass().func3()

# __pycache__と.pycファイルの生成回避
# python -B ファイル
# で実行する