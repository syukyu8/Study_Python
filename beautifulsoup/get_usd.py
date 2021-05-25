#BeautifulSoupインポート
from bs4 import BeautifulSoup
import urllib.request as req

#HTMLを取得
url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
res = req.urlopen(url)

#BeautifulSoupでHTMLを解析
soup = BeautifulSoup(res, "html.parser") #HTNLの解析にはhtml.parserを使うらしい

#欲しいデータを抽出
price = soup.select_one(".stoksPrice")
print("usd/jpy=", price.string)
