# -*- coding:utf-8 -*-
# クラスオブジェクト

# 座標クラス
class Coordinate:
    # コンストラクタ
    def __init__(self):
        self.x = 0
        self.y = 0
    
    # 平行移動メソッド
    def move(self, x, y):
        self.x += x
        self.y += y

    # 座標表示メソッド
    def show(self):
        print("(%0.2f, %0.2f)" % (self.x, self.y))
    
    # 文字列整形メソッド
    def __str__(self):
        # JavaのtoStringメソッドに相当
        return "({0},{1})".format(self.x, self.y)

# インスタンスを生成する方法
cood1 = Coordinate()    # インスタンス化
cood1.x = 1
cood1.y = 2
cood1.show()

# クラスをオブジェクトとして扱う
OBJ_C = Coordinate      # クラスオブジェクトを格納
cood2 = OBJ_C()         # オブジェクトからインスタンス化
cood2.x = 3
cood2.y = 4
cood2.show()
print()

# クラス属性
class MyClass():
    attr = "A"  # クラス変数(属性)

    def __init__(self):
        self.text = "sample text"

c1 = MyClass()
c2 = MyClass()
print("attr")
print(c1.attr, c2.attr, MyClass.attr)
# >> attr
# >> A A A

# MyClassそのもののクラス変数を変更する
MyClass.attr = "My Attr"
print("attr")
print(c1.attr, c2.attr, MyClass.attr)
# >> attr
# >> My Attr My Attr My Attr

# c1・c2には変数attrがまだ定義されていないため
# もともとのクラスのattrを探す
# そのため、未定義状態ではすべてのインスタンスに
# クラス変数の変更が反映される

# c1・c2のattrの値を変更する
c1.attr = "C1"
c2.attr = "C2"
# ここでc1・c2に変数attrが定義されるため
# 'C1'・'C2'を参照するようになる
print("attr")
print(c1.attr, c2.attr, MyClass.attr)
# >> attr
# >> C1 C2 My Attr
