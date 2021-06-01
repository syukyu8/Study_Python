import os
from scrapy.http import HtmlResponse
#chromedriverのパスがうまく通らないのでchromedriver_binaryをインポートする
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

folder = os.path.abspath("chromedriver")
#chromeを起動する
options = Options()
options.add_argument('-headless')
browser = webdriver.Chrome(chrome_options=options)

#URLを開く
def selenium_get(url):
    browser.get(url)

#CSSクエリが指定して読み込みが完了するまで待機
def get_dom(query):
    dom = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, query)
        )
    )
    return dom

#chromeを閉じる
def selenium_close():
    browser.close()

#ミドルウェアの本体
class SeleniumMiddleware(object):
    #リクエストをSeleniumで処理する
    def process_request(self, request, spider):
        browser.get(request.url)
        #取得したHTMLを返す
        return HtmlResponse(
            browser.current_url,
            body = browser.page_source,
            encoding = 'utf-8',
            request = request
        )