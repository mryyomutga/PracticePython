# -*- coding: utf-8 -*-

# 文字列の半角判定
# 半角英数字 
print("1a".isalnum()) # True
print("1a".isalpha()) # False
 
# 半角英字
print("a".isalnum()) # True
print("a".isalpha()) # True 
 
# 半角記号 
print("!".isalnum()) # False 
print("!".isalpha()) # False 
 
 
# 全角
print("あ".isalnum()) # True
print("あ".isalpha()) # True 
 
# utf-8に変換
# 半角英数字 
print("1a".encode('utf-8').isalnum()) # True
print("1a".encode('utf-8').isalpha()) # False
 
 
# 半角英字
print("1".encode('utf-8').isalnum()) # True 
print("1".encode('utf-8').isalpha()) # False
 
# 半角記号
print("!".encode('utf-8').isalnum()) # False 
print("!".encode('utf-8').isalpha()) # False
 
 
# 全角文字
print("あ".encode('utf-8').isalnum()) # False 
print("あ".encode('utf-8').isalpha()) # False 

# 文字列の数字判定
# 半角数字
print("1".isdigit()) # True
print("1".isdecimal()) # True
print("1".isnumeric()) # True
 
# 半角数値(符号付き)
print("0.01".isdigit()) # False 
print("0.01".isdecimal()) # False 
print("0.01".isnumeric()) # False 
  
# 半角数値(小数)
print("0.01".isdigit()) # False 
print("0.01".isdecimal()) # False 
print("0.01".isnumeric()) # False 
 
# U+0660を含む場合
print("0٠01".isdigit()) # True 
print("0٠01".isdecimal()) # True 
print("0٠01".isnumeric()) # True 
 
# 全角数字
print("１".isdigit()) # True
print("１".isdecimal()) # True
print("１".isnumeric()) # True
 
# 全角漢数字
print("百".isdigit()) # False 
print("百".isdecimal()) #  False
print("百".isnumeric()) # True
 
# 全角ローマ数字
print("Ⅳ".isdigit()) # False 
print("Ⅳ".isdecimal()) # False 
print("Ⅳ".isnumeric()) # True

# 文字列の数値変換
# 整数
integer_str = "100"
integer_num = int(integer_str)
print(integer_num)
 
# 小数
decimal_str = "1.55"
decimal_num = float(decimal_str)
print(decimal_num)

# 文字列の数値変換判定
def is_float_str(num_str, default=0):
    try:
        return {"is_float": True ,"val": float(num_str)}
    except ValueError:
        return {"is_float": False , "val": default}
          
print(is_float_str("1.5x"))
print(is_float_str("-1.5"))
print(is_float_str("1E16"))
