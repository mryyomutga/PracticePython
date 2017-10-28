# -*- coding:utf-8 -*-
# クラスの継承
# class クラス名(親クラス):
# スーパークラスを指定しない場合、objectクラスを自動的に継承する
class Parents(object):
    def func1(self):
        print("This is func1")

# ChildrenクラスはParentsクラスを継承
class Children(Parents):
    def func2(self):
        print("This is func2")

obj = Children()    # Childrenクラスをインスタンス化
obj.func1()         # 継承元のParentsクラスのメソッド呼び出し
obj.func2()         # Childrenクラスが持つメソッド
print()

# スーパークラスのメソッド呼び出し
class Parents(object):
    def func1(self):
        print("This is func1")

# ChildrenクラスはParentsクラスを継承
class Children(Parents):
    def func2(self):
        super().func1()   # Parentsクラスのfunc1メソッド呼び出し
        print("This is func2")

obj = Children()
obj.func1()     # Parentsクラスから継承したfunc1メソッド
obj.func2()     # Childrenクラスのfunc2メソッド
print()

# メソッドのオーバライド
class Parents(object):
    def func1(self):
        print("This is func1")

# ChildrenクラスはParentsクラスを継承
class Children(Parents):
    # Parentsクラスのfunc1メソッドをオーバライド
    def func1(self):
        print("This is func1(Override)")

obj = Children()
obj.func1()
print()

# 多重継承(非推奨)
class Parent1(object):
    def func1(self):
        print("This is \'Parent1 func1\'")

class Parent2(object):
    def func2(self):
        print("This is \'Parent2 func2\'")

# 継承するクラスをコンマ区切りで指定
class Children(Parent1, Parent2):
    def func(self):
        super().func1() # Parent1 - func1メソッドのオーバライド
        super().func2() # Parent2 - func2メソッドのオーバライド

obj = Children()
obj.func()