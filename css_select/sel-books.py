from bs4 import BeautifulSoup
fp = open("books.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

#CSSセレクターで10種類の方法で検索
sel = lambda q : print(soup.select_one(q).string)

#id属性がnuのもの
sel("#nu")

#id属性がnuで<li>タグがついたもの
sel("li#nu")

#<ul>タグの一階層下にある、id属性がnuで<li>タグがついたもの
sel("ul > li#nu")

#id属性がbibleの下にある、id属性がnuのもの
sel("#bible #nu")

#id属性がbibleの子であるid属性がnuのもの
sel("#bible > #nu")

#idがbibleである<ul>タグの直下にあるidがnuである<li>タグ
sel("ul#bible > li#nu")

#idがnuである<li>タグ
sel("li[id='nu']")

#4つ目の<li>を取り出す
sel("li:nth-of-type(4)")

#select()を使って<li>タグを全て取得し、[3]の要素を取得する
print(soup.select("li")[3].string)

#find_all()を使って<li>タグを全て取得し、[3]の要素を取得する
print(soup.find_all("li")[3].string)