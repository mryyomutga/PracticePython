# -*- coding:utf-8 -*-
# グローバル変数

x = 100
def sample():
    print(x)

sample()

x = 100
def sample():
    # 関数内ではローカル変数が出力される
    x = 200
    print(x)

sample()
# 関数の外ではグローバル変数が出力される
print(x)

print("関数内で変更")
# 関数内でグローバル変数を変更する方法
x = 100
def sample():
    global x    # グローバル変数であることを宣言する
    x = 200
    print(x)

sample()
print(x)
print()

# 関数オブジェクト
def sample():
    text = "sample"
    print(text)
    return "戻り値"

text = sample()
print(text)

f = sample  # 関数オブジェクトを格納
# 関数オブジェクトを実行
# 戻り値を変数に格納 
text = f()  
print(text)

# 関数の引数に関数を指定する
def param_func():
    print("param_func")
    return "sample"

def sample_func(f):
    x = f()
    print(x)    # param_func()の戻り値を出力

sample_func(param_func)
