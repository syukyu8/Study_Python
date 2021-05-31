from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USER = "JS-TESTER"
PASS = "ipCU12ySxI"

FAV_USER_ID = 32 #お気に入りをつけるユーザのID
SNS_URL = "https://uta.pw/sakusibbs/"

#chromeを起動する
options = Options()
options.add_argument('-headless')
browser = webdriver.Chrome(executable_path="./../chromedriver", chrome_options=options)

#ログインする
url_login = SNS_URL + "users.php?action=login"
browser.get(url_login)

#テキストボックスに文字を入力してフォーム送信する関数
def form_post(frm, d):
    for field, value in d.items():
        e = frm.find_element_by_name(field)
        e.clear()
        e.send_keys(value)
    frm.submit()

    #ページのロード完了まで待機
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".islogin")))

#対象となるフォームを指定
frm = browser.find_element_by_css_selector("#loginForm form")
#テキストボックスにデータを指定して送信する
form_post(frm, {
    "username_mmlbbs6":USER,
    "password_mmlbbs6":PASS
})

#本当にログインしたか画像で確認してみる
#どこまで処理が進んだか確認できる
browser.save_screenshot("sns-logined.png")

#本当にログインしたかHTMLで判断してみる
e = browser.find_element_by_id("bbsheader")
html = e.get_attribute("innerHTML")
#ログインできている時は、ヘッダ部分のHTML内にログアウトのためのリンクが表示されるのでそれをチェックする
if html.find("action=logout") < 0:
    print("ログインできていません")
    quit()
print("+ ログインしました")
time.sleep(1)

#ユーザのページ(作品一覧)を開く
url = SNS_URL + "users.php?user_id=" + str(FAV_USER_ID)
browser.get(url)

#作品一覧を得る
sakuhin_list = []
links = browser.find_elements_by_css_selector("ul#mmlist li a")

for a in links:
    href = a.get_attribute('href')
    title = a.text
    sakuhin_list.append((href, title))
print("+ 作品の一覧を{0}件取得しました".format(len(sakuhin_list)))

#一気にお気に入りを付ける
for href, title in sakuhin_list:
    #作品ページを開く
    print("- ", title)
    browser.get(href)
    
    try:
        #お気に入りボタンを押す
        e = browser.find_element_by_id("fav_add_btn")
        e.click()
        #お気に入りを取り消す場合
        #e = browser.find_element_by_id("fav_remove_btn")
        #e.click()

        print("| お気に入りにしました！")
    except:
        #お気に入りボタンがなかった時
        print("| 既にお気に入りでした.")
        #既に取り消し済みの場合
        #print("| 既に取り消し済みでした.")
    #負荷軽減
    time.sleep(1)