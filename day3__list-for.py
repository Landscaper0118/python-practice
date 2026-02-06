#　Day3:listとfor文の入力チェック練習

#listの使い方の確認
# food = ["ラーメン","餃子","肉まん"]

# for lanch in food:
#     print(lanch)

#forの使い方の確認
# old = [12,18,25,40]

# for check in old:
#     if check >= 20:
#         print(f"{check}は大人です")
#     else:
#         print(f"{check}は未成年です")

#以下はlistとforを使った応用練習
# point = [25,40,60,90]

# for correct in point:
#     if correct >= 60:
#         print(f"{correct}！合格！")
#     else:
#         print(f"{correct}!不合格！")

old =[10,13,20,35,69]

for tosi in old:
    if tosi >= 20:
        print(f"{tosi}歳は大人です")
    elif 12 <= tosi <= 19 :
        print(f"{tosi}歳は未成年です")
    else:
        print(f"{tosi}歳は子供です")
