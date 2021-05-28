#URLの一覧からリンク先を擬似的にダウンロードする Wikiはクローリング禁止なので
from urllib.parse import *
from urllib.request import *
from bs4 import BeautifulSoup
import os, os.path, time

#HTMLファイルの読み込み
html = open("eki-link.html", encoding="utf-8").read()

#HTMLを解析する
soup = BeautifulSoup(html, "html.parser")

#<a>タグを抽出する
links = soup.select("a[href]")

#（タイトル,　URL）のリストを作る
result = []
for a in links:
    href = a.attrs["href"]
    title = a.string
    result.append((title, href))

#リンク先をダウンロードする
savepath = "./out"
if not os.path.exists(savepath): os.mkdir(savepath)
for title, url in result:
    path = savepath + "/" + url + ".html"
    #相対URLを絶対URLに変換する
    a_url = urljoin("http://example.com", url)
    print("download=" + a_url)
    #ここでダウンロードをする
    #utlretrieve(a_url, path)
    time.sleep(1) 