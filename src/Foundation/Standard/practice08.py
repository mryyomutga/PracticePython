# -*- coding:utf-8 -*-
# while文
# 条件を満たす限りループするため、無限ループに注意する
i = 0
while i < 10:
    print(i)
    i += 1  # Pythonでインクリメントする場合`変数++`はエラーになる
print()

# 特定の文字列が入力されるまでループする
flag = True
while flag:
    print("文字を入力してください")
    c = input()
    # 文字列比較は`==`
    if c == "end":
        print(c + "が入力されたため終了します")
        flag = False
    else:
        print(c + "が入力されました")
print()

print("ループ処理を行う場合文字を入力してください")
is_conti = input() # ループ処理を続行するかどうかのフラグ
 
while is_conti:
    print('文字を入力してください')
    c = input()
 
    if c == 'end':
        is_conti = False
    else:
        print(c + 'が入力されました')
# 最初の処理で何も入力しない場合(条件がFalse)
# またはループを抜ける場合
else:
    print('処理を終了します')
print()

# ブロック内で処理を行わない場合
# passを記述することでエラーを回避する
x = 4
if(x >= 5):
    pass
else:
    print(x)