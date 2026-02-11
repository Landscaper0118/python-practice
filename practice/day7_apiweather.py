#openweather操作確認

import requests

#作成した自分のAPIキー(公開しない)
API_KEY = ""

lat = float(input("lat: "))
lon = float(input("lon: "))

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "units": "metric",
    "lang": "ja",
}

res = requests.get(url, params=params)
print("status:", res.status_code)

data = res.json()
print("raw:", data)

temp = data["main"]["temp"]
desc = data["weather"][0]["description"]
print("気温:", temp)
print("天気:", desc)

snow = data.get("snow")
rain = data.get("rain")

if snow is not None or data["weather"][0]["main"] == "Snow":
    print("判定: 雪の可能性あり（注意）")
elif data["main"]["temp"] <= 0 and (rain is not None or data["weather"][0]["main"] == "Rain"):
    print("判定: 気温0度以下＋雨 → 凍結リスクあり（注意）")
elif data["main"]["temp"] <= 0:
    print("判定: 気温0度以下 → 路面凍結の可能性あり")
else:
    print("判定: 大きな雪・凍結リスクは低そう")
