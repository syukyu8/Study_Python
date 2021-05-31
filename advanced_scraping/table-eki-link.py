#<table>タグを解析してCSV形式として出力する
from bs4 import BeautifulSoup
html = open("eki-link.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")

#出力用のリスト
result = []

#<table>タグを得る
table = soup.select_one("table")

#<tr>タグを得る
tr_list = table.find_all("tr")
#<tr>タグ要素の個数だけループ
for tr in tr_list:
    #<td>あるいは<th>タグを得る
    result_row = []
    #リストを与えることで複数のタグを一気に取得する
    td_list = tr.find_all(["td","th"])
    for td in td_list:
        #テキスト内容取得
        cell = td.get_text()
        result_row.append(cell)
    
    result.append(result_row)

#リストをCSV形式として出力する
for row in result:
    print(",".join(row))