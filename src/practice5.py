# -*- coding:utf-8 -*-
# Pythonのif-elif-else
# Pythonではスコープをインデント(タブ)で表す

if(10 > 5):
    # 条件が真であれば実行
    print("10は5より大きい")
print()

num1 = 8

if(num1 >= 10):
    print(str(num1) + "は10以上")
else:
    print(str(num1) + "は10より小さい")
print()

# `else if`ではなく`elif`を使う
# 論理和(||)は`or`演算子を使う
# 論理積(&&)は`and`演算子を使う
# 否定(!)は`not`演算子を使う

score = 86
absences = 0
print("欠席日数は" + str(absences) + "です")
if(absences < 6):
    print("あなたの評価点は" + str(score) + "です")
    if(score <= 100 and score >= 90):
        print("評価はS")
    elif(score < 90 and score >= 80):
        print("評価はA")
    elif(score < 80 and score >= 70):
        print("評価はB")
    elif(score < 70 and score >= 60):
        print("評価はC")
    else:
        print("評価はD")
else:
    print("出席日数が足りないため単位不認定となりました")
