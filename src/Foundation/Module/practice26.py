# -*- coding: utf-8 -*-
# if __name__=='__main__':の意味

from pkg1 import mod1

def func1():
    print("practice26.py : " + __name__)
    mod1.func1()

if __name__=="__main__":
    func1()

# 実行結果
# $ python practice26.py
#   __init__.py : pkg1
#   practice26.py : __main__
#   pkg1/mod1.py : pkg1.mod1

# $ python pkg1\mod1.py
#   pkg1/mod1.py : __main__