# -*- coding:utf-8 -*-
# プライベートメンバ
# アンダースコア2つ、末尾のアンダースコアが
# 1つ以内の変数をプライベートメンバとみなす

class Sample():
    def __init__(self):
        self.a = 0
        self._b = 0
        self.__c = 0    # プライベートメンバ
        self.__d_ = 0   # プライベートメンバ
        self.__e__ = 0

obj = Sample()
a = obj.a       # アクセス可能
b = obj._b      # アクセス可能
c = obj.__c     # AttributeError
d = obj.__d_    # AttributeError
e = obj.__e__   # アクセス可能