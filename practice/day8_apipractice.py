#cities = ["Tokyo", "Osaka", ...]     get_weather は以下を返す（統一）
#for 文で回す                      　  成功：(temp, None)
#temp があれば表示                     失敗：(None, "ERROR_TYPE") 
#失敗なら「都市名 + エラー」を表示       
#1都市失敗しても続行 

import requests
# #作成した自分のAPIキー(公開しない)
API_KEY = "dfb92224b04450fde1497dd3d1744395"
url = "https://api.openweathermap.org/data/2.5/weather"
#都市の格納場所
cities = ["Tokyo","Osaka","Fukuoka","Sapporo","Niigata"]

def get_weather(city,api_key,url):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
}
#接続状況を確認する
    try:
        response = requests.get(url,params=params,timeout=10)
#接続エラーが発生したら以下を返す
    except requests.exceptions.RequestException:
        return None,"NETWORK_ERROR"
#200(正常)以外の時にエラーコードを返すようにする+APIエラーメッセージを拾う
    if response.status_code != 200:
        msg = None
        try:
            msg = response.json().get("messege")
        except (ValueError,TypeError,AttributeError):
            pass
        if msg:
            return (None,f"HTTP_ERROR_{response.status_code}:{msg}")
        return (None,f"HTTP_ERROR_{response.status_code}")
    try:
        data = response.json()
        temp = data["main"]["temp"]
#データ構想が想定と違った際に以下を返す
    except (ValueError, KeyError, TypeError):
        return None, "DATA_ERROR"
#エラーが発生しなかった場合に返す処理
    return(temp,None)

#変数citiesに記載した都市名を順番に処理する
for city in cities:
    temp,error = get_weather(city,API_KEY,url)
#Tempが正常が正常に返って来た時の処理
    if temp is not None:
        print(f"{city}の気温:{temp}℃")
#エラー発生時(Noneで返ってきた時)
    elif error is "HTTP_ERROR_401":
        print("APIキーを確認")
    elif error is "HTTP_ERROR_429":
        print("回数制限")
    else:
        print(f"{city}:{error}")