from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USER = "JS-TESTER"
PASS = "ipCU12ySxI"

#chromeを起動する
options = Options()
options.add_argument('-headless')
browser = webdriver.Chrome(executable_path="./../chromedriver", chrome_options=options)

#ログインページにアクセス
url_login = "https://uta.pw/sakusibbs/users.php?action=login"
browser.get(url_login)
print("ログインページにアクセスしました")

#テキストボックスにUSERを入力する
#id属性userから要素を取得
e = browser.find_element_by_id("user")
#e.clear()
e.send_keys(USER)

#テキストボックスにPASSを入力する
#id属性passから要素を取得
e = browser.find_element_by_id("pass")
#e.clear()
e.send_keys(PASS)

#ログインフォームを探す
frm = browser.find_element_by_css_selector("#loginForm form")
#フォームの内容を送信
frm.submit()
print("情報を入力してログインボタンを押しました")

#ページのロードまで待機(.isloginというクラスが現れるまで)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".islogin")))

#マイページのURLを得る
a = browser.find_element_by_css_selector(".islogin a")
url_mypage = a.get_attribute('href')
print("マイページのURL=", url_mypage)

#マイページを表示
browser.get(url_mypage)

#お気に入りのタイトルを列挙
links = browser.find_elements_by_css_selector("#favlist li > a")
for a in links:
    href = a.get_attribute('href')
    title = a.text
    print("-", title, ">", href)