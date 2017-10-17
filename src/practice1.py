# 基本的な変数・数値の操作
# コメントは`#`を付ける
print("Hello World")

# 数値計算
print(10 + 2)
print(10 - 2)
print(10 * 2)
print(10 / 2)
print(10 % 2)
print(10 ** 2)

# 変数
num = 5
num1 = 3.1415
num2 = "変数"
num3 = False

print(num)
print(num1)
print(num2)
print(num3)

num += num1
print(num)

# 型(type)
num = 5
print(type(num))
print(type(num1))
print(type(num2))
print(type(num3))

# 型変換
e1 = int(3.14)
print(e1)

e2 = int(True)
print(e2)

e3 = int(False)
print(e3)

e4 = int('100')
print(e4)

e5 = int("-99")
print(e5)

# int()などを使用せずに変換
e6 = True + 2
print(e6)