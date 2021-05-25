from bs4 import BeautifulSoup
fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

#CSSセレクターを使った4種類の抽出
#全ての<li>タグの中から8個目の要素を取り出す
print(soup.select("li")[7].string)


#print(soup.select_one("li:nth-of-type(8)").string) 
#これだと失敗する nth-of-type(4)までは動くが、nth-of-type(5)にするとve-list直下の<li>タグの5個目と認識してしまう
#nth-of-type(6)以降はエラー


#idがve-listの直下にある<li>タグの4個目を取り出す
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)

#idがve-listの直下にある<li>タグのうち、data-lo属性が"us"のもので、[1]の要素を取り出す
print(soup.select("#ve-list > li[data-lo='us']")[1].string)

#idがve-listの直下にあるclassが"black"の中の[1]の要素を取り出す
print(soup.select("#ve-list > li.black")[1].string)

#find()で取り出す
#data-lo属性が"us"でclass属性が"black"と指定する
cond = {"data-lo":"us", "class":"black"}
print(soup.find("li", cond).string)

#find()を2度使う
#先にve-listの要素を抽出し、さらにdata-lo属性が"us"でclass属性が"black"と指定する
print(soup.find(id="ve-list").find("li", cond).string)