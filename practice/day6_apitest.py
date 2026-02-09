#APIとは データだけ返すプログラム専用の場所　画面はなくjson形式で多くが管理されている
#例：天気や地図などをgoogleやopenweatherといったAPIからデータをもらう

#webにアクセスするライブラリを導入する(requests)
#python -m pip install repuests でインストール可能(初回のみ)

#urlがAPIかWebサイトかはブラウザを開いて文字だけで構成されていたり
# #"name"や"xxx"などといった記載がある場合にはAPIの可能性が高い
#WEBサイトの場合ロゴや検索欄などが表示されたり見せるために画面が整えられていることがある

#import requestsでHTTP通信を行うためのライブラリを読み込む
#htto通信とはインターネット上でリクエストとレスポンスをやり取りする
# import requests
# #下記はname=任意の名前から平均年齢を統計から推測してデータを返してくれるAPI
# url = "https://api.agify.io?name=hanako"

# #urlにデータ取得リクエストを送りWebからデータを受け取る
# response = requests.get(url)

# #通信が成功したか確認する
# # 1xx 処理中
# # 2xx 成功
# # 3xx リダイレクト(別の場所へ)
# # 4xx クライアントエラー(リクエスト不備)
# # 5xx サーバー側エラー
# print(response.status_code)

# #APIから帰ってきたjson文字列を辞書(dict)に変換
# data = response.json()

# #dictに登録した辞書の中身を取り出して表示
# print(data)
# print(data["name"])
# print(data["age"])

#chatgptからの問題
#inputで名前を受けてAPIを叩くコード

import requests

name = input("名前を入力してください")

url = f"https://api.agify.io?name={name}"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data)
print(data["name"])
print(data["age"])
#呼び出せるがひらがなや漢字などを使用するとリクエストは返ってくるのにcountやageに何も返ってきてないのが気になった
#サイトが英語圏の名前データが中心で日本語の統計がないのが理由
# #付け足すならdata下を以下に変更することで実務っぽい処理になる
# age = data["age"]

# if age is None:
#     print("年齢データが見つかりませんでした")
# else:
#     print(f"{name} の推定年齢は {age} 歳です")