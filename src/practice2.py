# 文字列の基本的な操作

# 文字列変換
print(str(3))

print(str(2.5))

print(str(True))

# エスケープ文字
s = "Hello!\nHow are you?"
print(s)

# 文字列の連結
s1 = "abc"
s2 = "def"
print(s1, s2)
print(s1 + s2)

# 文字列の繰り返し var * n
s3 = "loop"
print(s3 * 3)

# 文字の抽出 var[n]
s4 = "abcdef"
print(s4[0])    # a
print(s4[1])    # b
print(s4[2])    # c
print(s4[-1])   # f
print(s4[-2])   # e

# 文字列のスライス var[:]
# 文字列変数[start:end:step]
# endを指定した場合end-1文字目までをスライスする
test = "abcdefghijklmn"
print("test[:] = " + test[:])
print("test[2:] = " + test[2:])
print("test[:2] = " + test[:2])
print("test[2:5] = " + test[2:5])
print("test[0:5:2] = " + test[0:5:2])
print("test[-1::-1] = " + test[-1::-1])

# 文字列の長さの取得 len()
s5 = "xx大学yy学部zz学科"
print(len(s5))

# 文字列の分割 var.split()
# セパレータを指定しない場合、改行・スペース・タブをセパレータにする
s6 = "こんにちは。文字列に関するプログラムです。Python3で実行できます。"
print(s6.split("。"))

# 文字列の置換 var.replace()
s7 = "Python3系を使ってはいけない"
print(s7.replace("3", "2"))
