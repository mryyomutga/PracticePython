# -*- coding:utf-8 -*-
# ジェネレータ
# 処理の途中で値を返し、必要に応じて処理を再開できる
def sample_generator():
    print("call 1")
    yield "1st step"
    print("call 2")
    yield "2nd step"
    print("call 3")
    yield "3rd step"

# ジェネレータオブジェクトを作成
gen_func = sample_generator()

text = gen_func.__next__()  # yieldまで実行
print(text)     # 1st step

text = gen_func.__next__()
print(text)     # 2nd step

text = gen_func.__next__()
print(text)     # 3rd step
print()

# ループ処理でジェネレータ関数を実行
def sample_generator():
    print("call 1")
    yield "1st step"
    print("call 2")
    yield "2nd step"
    print("call 3")
    yield "3rd step"

gen_func = sample_generator()

for text in gen_func:
    print(text)

# フィボナッチ数列を返すジェネレータ
def fibonacci_generator():
    f0, f1 = 0, 1
    while True: # この中が10回繰り返される
        yield f0
        f0, f1 = f1, f0 + f1
 
gen_func = fibonacci_generator()
 
for i in range(0, 10):
    # 10個取得する
    num = next(gen_func)
    print(num)
print()

# send()メソッド
# 待機中のジェネレータに値を設定する
def sample_generator():
    text = yield "Good Morning"
    yield text
    yield text

gen_func = sample_generator()
text = next(gen_func)
print(text)

text = gen_func.send("Hello")
print(text)

text = next(gen_func)
print(text)

# thorw()メソッド
# 待機中のジェネレータに例外を送信

# close()メソッド
# 待機中のジェネレータを正常終了させる
