# -*- coding:utf-8 -*-
# classの基本

# class クラス名:
# 内部からアクセスする場合、self.メンバ変数
# メソッドはクラスで定義された関数

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

# インスタンス化
cood = Coordinate()
# 外部からメンバ変数にアクセスする
cood.x = 100
cood.y = 200

# Coordinateクラスのshowメソッドの利用
cood.show()

# 整形した文字列の取得
form = cood.__str__()
print(form)
print()

# インスタンスの操作
class Sample:
    def __init__(self):
        self.x = 100

obj = Sample()
obj.y = 200     # メンバ変数yを追加
print(obj.x, obj.y)

del obj.x       # メンバ変数xの削除
# print(obj.x)  # エラー
# Traceback (most recent call last):
#   File "practice13.py", line 52, in <module>
#     print(obj.x)
# AttributeError: 'Sample' object has no attribute 'x'
print()

# 空のクラス
class Empty:
    pass

emp = Empty()
# 空のクラスにメンバ変数を追加する
emp.x = 10
emp.y = 20
print(emp.x, emp.y)
