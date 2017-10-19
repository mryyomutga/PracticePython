# -*- coding:utf-8 -*-
# 内部関数の定義

def outer_function():
    print("Run outer_function")

    # 関数内部で関数を定義する
    def inner_function():
        print("Run inner_function")

    inner_function() # 内部関数の実行
    print("Finished inner_function")

outer_function()
print("Finished outer_function")
print()

# 関数オブジェクトを用いる
def outer_function():
    print("Run outer_function")

    def inner_function():   # 内部関数
        print("Run inner_function")

    f = inner_function
    print("End outer_function")

    return f    # 内部関数を関数オブジェクトとして返す

# 外部関数を実行
f = outer_function()
f()     # 内部関数を実行 
print()

# nonlocal宣言
# 内部関数から外部のローカル変数を参照する
def outer_function():
    print("Run outer_function")
    x = 100
    print(x)    # x = 100

    def inner_function():
        print("Run inner_function")
        nonlocal x  # outer_functionで定義されているxを参照
        x = 200
        print(x)    # x = 200

    inner_function()
    print("Finished inner_function")

    # inner_functionでx=200に変更
    print(x)    # x = 200

outer_function()
print("Finished outer_function")
print()
