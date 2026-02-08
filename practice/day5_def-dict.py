# #defの基礎練習
# #nameという箱を持ったgreetという[関数を作る(def)]
# def greet(name):
#     print(f"{name}さん,こんにちは")
# #greet後の()に名前や数字などを入れるとそれが関数に入る
# greet("太郎")
# greet("花子")

# #returnについて
# #以下は関数aとbに入れた数字を計算する。returnによって計算結果が関数外に返る
# def add(a,b):
#     result = a + b
#     return result
# #ここで数字を指定する(add[3,5]の部分)と計算されその結果がprintによって計算結果が表示される
# total = add(3,5)
# print(total)

#ifなどで複数returnで返すことができるがreturn後にprintなどを記載しても関数が終了しているため実行されなくなる(以下例文)
# def test():
#     print("A")
#     return
#     print("B")

# test()

# def judge(age):
#     if age >= 20:
#         return "大人"
#     else:
#         return "未成年"

#chatgptの問題
#数字2つを受け取って 足し算の結果を return する関数 を作ってください。

# def add(a,b):
#     result = a + b
#     return result

# #計算するためにはint式に変える必要がある
# x = int(input("一つ目の数字を入れてください："))
# y = int(input("二つ目の数字を入れてください："))

# #resultはadd関数内の変数のため関数外で使えないため、別の変数などでreturnされたものを受け取る必要がある
# total = add(x,y)
# print(f"足した結果は{total}です")

#chatgptの問題
#年齢を渡すと「20以上なら大人」か「それ以外は未成年」を返す関数を作ってください

# def judge_age(age):
#     if age >= 20:
#         return "大人"
#     else:
#         return "未成年"

# x = int(input("年齢を入力してください："))

# result = judge_age(x)

# print(result)

#chatgptの問題
#金額を渡すと送料を返す関数を作ってください。
#5000以上 → 0 / 2000以上 → 300 / それ未満 → 500  printじゃなくてreturnで返すこと。
# def money(judge):
#     if judge >= 5000:
#         return 0
#     elif judge >= 2000:
#         return 300
#     else:
#         return 500
    
# x = int(input("金額を入力して下さい："))

# total = money(x)
# print(f"送料は{total}円です")

# #dictの基礎練習
# #辞書(item)の中にキー(name,price)と値(リンゴ,120)を複数持つことが可能
# item = {"name": "りんご", "price": 120}
# 
# #辞書名+キー名を指定することでキーに入っている値を取り出して表示できる
# print(item["name"])
# print(item["price"])

#chatgptの問題
#次を満たす person 辞書を作ってください。
#name：自分の名前（文字）/ age：年齢（数字）その後 print()でname を表示 / age を表示

# person ={
#     "name":"庭師",
#     "age":24
# }

# print(person["name"])
# print(person["age"])

#chatgptの問題
#次の辞書 scores を作ってください。
#math：70 / english：55 / science：90 その後 for を使って：60以上 → 「合格」 / それ以外 → 「不合格」

scores ={
    "math":70,
    "english":55,
    "science":90
}
#point変数を作成しないと文字列を取ってきてしまうため、計算ができなくなりエラーになる。
for judge in scores:
    point = scores[judge]

    if point >= 60:
        print(f"{judge}{point}点:合格!")
    else:
        print(f"{judge}{point}点:不合格……")