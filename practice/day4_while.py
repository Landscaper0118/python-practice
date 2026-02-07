#whileの入力チェック練習
# count = 1

# while count <=3:
#     print(count)
#     count += 1py

#以下はwhileの応用練習
#while count >= 3だと3以上を入力すると終了と表示される
#   else: print("1~3の数字を入力して下さい")と記載すれば4以上は数字の入力を求められる
# count = 0

# while count != 3:
#     count = int(input("1:開始 2:設定 3:終了"))
#     if count == 1:
#         print(f"{count}:開始")
#     elif count == 2:
#         print(f"{count}:設定")
#     elif count == 3:
#         print(f"{count}:終了")
#     else:
#         print("1~3の数字を入力して下さい")

# age = 0  

# while age != -1:
#     age = int(input("年齢を入力してください（終了するには -1）: "))
    
#     if age == -1:
#         print("終了します")
#     elif age >= 20:
#         print(f"{age}歳は大人です")
#     elif 13 <= age <= 19:
#         print(f"{age}歳は未成年です")
#     else:
#         print(f"{age}歳は子どもです")

#break trueの練習
# num = 1

# while True:
#     num = int(input("1:開始 2:設定 3:終了 "))

#     if num == 1:
#         print(f"{num}:開始")
#     elif num == 2:
#         print(f"{num}:設定")
#     elif num == 3:
#         print("終了しました")
#         break
#     else:
#         print("1〜3を入力してください")

age = 0

while True:
    age = int(input("年齢を入力してください(-1で入力を終了)"))
    if age == -1:
        print("終了しました")
        break
    elif age >= 20:
        print(f"{age}歳は大人です")
    elif 13 <= age <= 19:
        print(f"{age}歳は未成年です")
    elif 0 <= age <= 12:
        print(f"{age}歳は子供です")
    else:
        print("無効な入力です")