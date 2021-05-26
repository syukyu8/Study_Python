#作詞掲示板にログインしてお気に入りの詞を取得する
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#ユーザ名とパスワードの指定
USER = "JS-TESTER"
PASS = "ipCU12ySxI"

#セッション開始
session = requests.session()

#ログインの情報
login_info = {
    "username_mmlbbs6": USER, #ユーザ名を指定
    "password_mmlbbs6":PASS, #パスワードを指定
    "back":"index.php", #ログイン時に指定する値
    "mml_id":"0" #ログイン時に指定する値
}
url_login = "https://uta.pw/sakusibbs/users.php?action=login&m=try"
#POSTしてwebページを取得する
res = session.post(url_login, data=login_info)
res.raise_for_status() #ステータスコードが200番台以外の場合、例外を発生させる

#マイページのURLを取得する
soup = BeautifulSoup(res.text, "html.parser")
a = soup.select_one(".islogin a")
#取得に失敗した時
if a is None:
    print("マイページが取得できませんでした")
    quit()

#相対URLを絶対URLに変換
url_mypage = urljoin(url_login, a.attrs["href"])
print("マイページ=", url_mypage)

#マイページにアクセス
res = session.get(url_mypage)
res.raise_for_status()

#お気に入りの詞のタイトルを列挙
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select("#favlist li > a")
for a in links:
    href = a.attrs["href"]
    title =  a.get_text()
    print("-", title,  ">", href)