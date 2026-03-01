#cities = ["Tokyo", "Osaka", ...]     get_weather は以下を返す（統一）
#for 文で回す                      　  成功：(temp, None)
#temp があれば表示                     失敗：(None, "ERROR_TYPE") 
#失敗なら「都市名 + エラー」を表示       
#1都市失敗しても続行 

import requests

API_KEY = ""
url = "https://api.openweathermap.org/data/2.5/weather"
cities = ["Tokyo", "Osaka", "Fukuoka", "Sapporo", "Niigata"]

def get_weather(city, api_key, url):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    # 通信エラー対策：timeoutは必須
    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException:
        return None, "NETWORK_ERROR"

    # HTTPエラー
    if response.status_code != 200:
        # 可能ならAPIのエラーメッセージも拾う
        msg = None
        try:
            msg = response.json().get("message")
        except (ValueError, TypeError, AttributeError):
            pass

        if msg:
            return None, f"HTTP_ERROR_{response.status_code}:{msg}"
        return None, f"HTTP_ERROR_{response.status_code}"

    # JSON/データ構造エラー
    try:
        data = response.json()
        temp = data["main"]["temp"]
    except (ValueError, KeyError, TypeError):
        return None, "DATA_ERROR"

    return temp, None
#現状だとエラーコードを追加する度にelifに追加しなければいけないため、管理ができなくなる(記載漏れやスペルミス等)
for city in cities:
    temp, error = get_weather(city, API_KEY, url) 
    if temp is not None: 
        print(f"{city:<10} | {temp}℃") 
    else: 
        code = error.split(":",1)[0] if error else "UNKNOWN_ERROR" 
        
        if code == "HTTP_ERROR_401": 
            print(f"{city:<10} | ERROR: APIキーを確認 ({error})") 
        elif code == "HTTP_ERROR_429": 
            print(f"{city:<10} | ERROR: 回数制限 ({error})") 
        else: 
            print(f"{city:<10} | ERROR: {error}")
        