from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import zipfile

#XMLをダウンロード
url = "https://www.city.yokohama.lg.jp/kurashi/bousai-kyukyu-bohan/bousai-saigai/bosai/data/data.files/shelter.zip"
savezip = "shelter.zip"
savename = "shelter.xml"
if not os.path.exists(savezip):
    req.urlretrieve(url, savezip)

#zip解凍
with zipfile.ZipFile(savezip, 'r') as zf:
    zf.extractall('./')

#BeautifulSoupで解析
xml = open(savename, "r", encoding="utf=8").read()
soup = BeautifulSoup(xml, 'html.parser')

#データを各区ごとに確認
#XMLで使われる<Shelter>や<Name>タグもHTMLと見なして解析されるので全て小文字に変換されることに注意
#任意の要素にアクセスする時は全て小文字でタグを指定する！
info = {}
for i in soup.find_all("shelter"):
    name = i.find('name').string
    ward = i.find('name').string
    addr = i.find('address').string
    note = i.find('notes').string
    if not (ward in info):
        info[ward] = []
    info[ward].append(name)

#区ごとに防災拠点を表示
for ward in info.keys():
    print("+", ward)
    for name in info[ward]:
        print("| - ", name)