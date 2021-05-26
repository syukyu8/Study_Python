#Pythonのマニュアルを再帰的にダウンロードする
from  bs4 import  BeautifulSoup
from urllib.request import *
from urllib.parse import *
#ディレクトリを作成するためのos
from os  import makedirs
#スリープのためのtime
import os.path, time, re

#解析済みかどうか判断する変数
proc_files = {}

#HTMLを解析してリンクを抽出する関数
def enum_links(html, base):
    #CSSとリンクを抽出する
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    result =  []

    #href属性にあるリンクを取り出し、絶対パスに変換する
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result

#ファイルをダウンロードする関数
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc +  o.path
    #文字列の末尾が"/"つまりディレクトリならindex.htmlを追加する
    if re.search(r"/$", savepath):
        savepath += "index.html"
    #パスからフォルダ名を取得
    savedir = os.path.dirname(savepath)

    #パスが存在している（既にダウンロード済み）場合
    if os.path.exists(savepath): return savepath

    #ディレクトリが存在しない場合、ダウンロード先のディレクトリを作成
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)

    #ファイルをダウンロードする
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1) #1秒スリープは礼儀らしい
        return savepath
    except:
        print("ダウンロード失敗:", url)
        return None

#HTMLを解析してダウンロードする関数
def analize_html(url, root_url):
    #download_file関数呼び出し、ダウンロードしたファイルが存在しない、または解析済みなら処理しない
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return
    #このファイルは解析済みと印をつける
    proc_files[savepath] = True
    print("analize_html=", url)

    #リンクを抽出する
    html = open(savepath, "r", encoding="utf-8").read()
    #enum_links関数呼び出し
    links = enum_links(html, url)

    for link_url in links:
        #リンクがルート以外のパスを指していた場合はダウンロードしないようにする
        if link_url.find(root_url) != 0:
            #cssファイルはダウンロードしたいので、それ以外の場合は次のループへ
            if not re.search(r".css$", link_url): continue
        #HTMLかどうか
        if re.search(r".(html|htm)$", link_url):
            #再帰的にHTMLファイルを解析
            analize_html(link_url, root_url)
            continue
        #それ以外のファイル
        download_file(link_url)

if __name__ == "__main__":
    #URLを全てダウンロードする
    url = "https://docs.python.jp/3.6/library/"
    analize_html(url, url)