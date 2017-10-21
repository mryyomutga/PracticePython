# -*- coding:utf-8 -*-
# 例外処理

param ={'x':1000, 'y':10}
# 例外発生の可能性がある箇所をtryブロック内に記述
try:
    x = param['x']
    y = param['y']
    z = x / y
    print(z)

# except Error as e:で例外のキャッチ
except KeyError as e:
    print("データが存在しません")
    print(type(e), str(e))
except ZeroDivisionError as e:
    print("0で除算しました")
    print(type(e), str(e))
except :
    print("予期せぬ例外が発生しました")
# 例外が発生しなかった場合
else:
    print("elseブロックに到達")
# 例外発生の有無にかかわらず実行
finally:
    print("finallyブロックの実行")

# 例外送出
# raise 例外クラス・例外オブジェクト

# 10倍する関数
def sample(num):
    if type(num) != int:    # 引数がint型でない場合
        raise TypeError("不正なパラメータ", num)
    
    return num * 10

print(sample(10))
# print(sample(10.0))

# 独自の例外定義
# Exceptionクラスを継承する
class ParamError(Exception):
    pass

def sample(num):
    if type(num) != int:
        raise ParamError("不正なパラメータ")

    return num * 10

print(sample(10))
# print(sample(10.0))