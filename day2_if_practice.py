money = input("金額を入力してください(5000円以上は送料無料!):")

if not money.isdigit():
    print("数字で入力してください")
else:
    money = int(money)

    if money <= 0:
        print("不正の金額です")
    elif money < 2000:
        print("送料500円")
    elif  money < 5000:
        print("送料300円")
    else:
        print("送料無料")
