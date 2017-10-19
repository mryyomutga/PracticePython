# -*- coding:utf-8 -*-
# 関数の定義
# def 関数名(引数1, 引数2, 引数3,...):

# 引数同士足し合わせる関数
def add(x, y):
    z = x + y
    return z    # 値を返す場合return文を使う

# 引数の値を出力する関数
def output1(arg1, arg2):
    print(arg1, arg2)

# 引数の値を出力する関数
# デフォルトで引数に値を設定すると、呼び出す際に値を設定しなくてもよい
def output2(arg1, arg2 = "y", arg3 = "z"):
    print(arg1, arg2, arg3)

# add関数の実行
# !! 関数を定義してから呼び出す(関数の下で呼び出す)
x = 1
y = 2
num = add(x, y)
print("x :", x)
print( "y :", y)
print("num :", num)

# 引数を与える場合
# 順番に引数を指定する
output1("a", "b")

# キーワード引数(引数名=値)で順序を無視する
output1(arg1="c", arg2="d")  # キーワードを指定
output1(arg2="f", arg1="e")  # キーワード引数は順序を無視する

# 引数全てに値を設定
output2("a", "b", "c")
# 3番目の引数を省略
output2("c", arg2 = "d")
# 2,3番目の引数を省略
output2("e")
# returnがない関数は`None`が返される
print(output2("x"))

# 可変長引数
# def 関数名(引数1, 引数2, *引数シーケンス, **引数辞書)
# 引数シーケンス
print("argument sequense")
def samp_func1(arg1, *arg2):
    print(arg1, arg2)

# 可変長にタプルとして格納される
samp_func1("a", "b", "c", "d")

# 引数辞書
def samp_func2(arg1, **arg2):
    print(arg1, arg2)

# キーワード引数が可変長に辞書として格納される
samp_func2("a", key1 = "b", key2 = "c", key3 = "d")

# 呼び出されるたびにデフォルト引数の値が変更される
def sample(x, arg=[]):
    arg.append(x)
    return arg
 
print(sample(1)) # [1]
print(sample(2)) # [1, 2]
print(sample(3)) # [1, 2, 3]

# デフォルト引数にイミュータブルなものに変更する
def sample(x, arg=None):
    if arg is None:
        arg = []
 
    arg.append(x)
    return arg
 
print(sample(1)) # [1]
print(sample(2)) # [2]
print(sample(3)) # [3]
