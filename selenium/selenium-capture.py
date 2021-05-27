#webブラウザを遠隔操作するツールSeleniumのインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

#ヘッドレスモードを有効にする
options = Options()
options.add_argument('-headless')

#chromeを起動する
browser = webdriver.Chrome(executable_path="./../chromedriver", chrome_options=options)

#URLを読み込む
browser.get(url)

#画面をキャプチャーし、ファイルに保存する
browser.save_screenshot("website.png")

#ブラウザ終了
browser.quit()