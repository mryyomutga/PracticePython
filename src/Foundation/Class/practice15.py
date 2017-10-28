# -*- coding:utf-8 -*-
# クラスメソッド
# メソッド内で自身を参照できるメソッド
# スタティックメソッド
# クラスに依存しないメソッド

import math # mathモジュールのインポート

class Coordinate:
    class_var = "hoge"  # クラス変数

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

    # クラスメソッド
    # 第1引数はクラス自身を表すclsを指定
    # 生成したオブジェクトを返すメソッド
    @classmethod
    def class_method(cls, x, y):
        new_cood = cls()    # 新しくインスタンス生成
        new_cood.x = x
        new_cood.y = y
        return new_cood

    # スタティックメソッド
    # メンバ変数にアクセス不可のためself不要
    # 2点間の距離を返すメソッド
    # 必要性の感じられないメソッドらしい
    @staticmethod
    def static_method(cood1, cood2):
        x = cood1.x - cood2.x
        y = cood1.y - cood2.y
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

cood1 = Coordinate()    # インスタンス化
cood1.x = 0
cood1.y = 0
cood1.show()

# クラスメソッドを用いて新たにオブジェクトを生成
cood2 = cood1.class_method(1, 1)
cood2.show()

# スタティックメソッドを用いて距離を算出
dist = Coordinate.static_method(cood1, cood2)
print("distance=%f" % dist)

# 
dist = cood1.static_method(cood1, cood2)
print(dist)
