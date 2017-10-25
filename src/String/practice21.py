# -*- coding: utf-8 -*-
# 文字列をリストと結合
# 結合文字.join(リスト)
data = ["aaa", "bbb", "ccc", "ddd", "eee"]
csv = ",".join(data)    # リスト内の要素をコンマ区切りで結合
print(csv)

# 分割
data = "aaa bbb ccc ddd eee"
data_list = data.split(" ")  # 文字列を空白文字で区切る
print(data_list)

# 置換
# 元の文字列.replace(置換前文字列, 置換後文字列)
text = "xxxbbbccc"
new = text.replace("x", "a")    # xをaに置換
print(text)
print(new)

# 場所を指定して文字を取得
text = "abcdefghijklmn"
print(text[0])
print(text[3])
print(text[-1])     # 末尾から数えて1番目の文字を取得

# 指定した文字列が含まれているか判定
text = "abcdefg"
print("cde" in text)    # "cde"という文字列が含まれているか

# 文字列のループ処理
text = "abdcefghijklmn"
for s in text:
    print(s)

# 文字列の検索
text = "abcabc"
print(text.find("bc"))  # 先頭から検索
print(text.rfind("bc")) # 末尾から検索

# 文字列のトリミング
text = " abcabc "
print(text.strip())     # 空白を除去
print(text.lstrip())    # 左側を除去
print(text.rstrip())    # 右側を除去

# 大文字・小文字変換
text = "abcDEF"
print(text.upper())
print(text.lower())
print(text.capitalize())    # 先頭だけ大文字に変換
