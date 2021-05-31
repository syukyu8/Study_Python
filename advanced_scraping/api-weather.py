import requests
import json

#APIキーの指定
apikey = "API"

#天気を調べたい都市の一覧
cities = ["Tokyo,JP", "London,UK", "New York,US"]

#APIのひな型
api = "https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

#温度変換（ケルビン→摂氏に変換する必要あり）
#lambda式で気温データを摂氏に変換する関数を定義する
k2c = lambda k:k - 273.15

#各都市の温度を取得する
for name in cities:
    #APIのURLを得る
    url = api.format(city=name, key=apikey)
    #実際にAPIリクエストして結果を取得する
    r = requests.get(url)
    # 結果はJSON形式なのでデコードする
    data = json.loads(r.text)
    #結果を画面に表示する
    print("+都市=", data["name"])
    print("|天気=", data["weather"][0]["description"])
    print("|最低気温=", data["main"]["temp_min"])
    print("|最高気温=", data["main"]["temp_max"])
    print("|湿度=", data["main"]["humidity"])
    print("|気圧=", data["main"]["pressure"])
    print("|風速度=", data["wind"]["speed"])
    print("")