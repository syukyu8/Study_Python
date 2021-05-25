#ライブラリのインポート
#コマンドライン引数を得るためのsys
import sys
#データをダウンロードする用
import urllib.request as req #urllib.requestをreqという名前で使用する
#リクエスト用のパラメータをURLエンコードする用
import urllib.parse as parse #urllib.parseをparseという名前で使用する

#コマンドライン引数を得る
if len(sys.argv) <= 1:
    #長さ1だと実行ファイル名しか入力されていない
    print("USAGE: hyakunin.py (keyword)")
    #プログラムを終了させる
    sys.exit()
keyword = sys.argv[1]

#パタメータをURLエンコードする
#APIエントリーポイントを指定
API = "https://api.aoikujira.com/hyakunin/get.php"

#パラメータ設定
query = {
    "fmt":"ini",
    "key": keyword
}
#urlencodeを使ってURLエンコード
params = parse.urlencode(query)
#リクエスト用のURLを生成
url = API + "?" + params
print("url=", url)

#ダウンロード
with req.urlopen(url) as r:
    #データ読み込み
    b = r.read()
    #文字列形式に変換する
    data = b.decode('utf-8')
    print(data)
