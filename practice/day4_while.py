#whileの入力チェック練習
# count = 1

# while count <=3:
#     print(count)
#     count += 1py

#以下はwhileの応用練習
#while count >= 3だと3以上を入力すると終了と表示される
#   else: print("1~3の数字を入力して下さい")と記載すれば4以上は数字の入力を求められる
count = 0

while count != 3:
    count = int(input("1:開始 2:設定 3:終了"))
    if count == 1:
        print(f"{count}:開始")
    elif count == 2:
        print(f"{count}:設定")
    elif count == 3:
        print(f"{count}:終了")
    else:
        print("1~3の数字を入力して下さい")