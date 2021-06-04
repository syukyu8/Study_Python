#ライブラリのインポート
import MySQLdb

#MySQLに接続する
conn = MySQLdb.connect(
    user='root',
    passwd='test-password', #それぞれがmysqladminで設定したパスワード
    host='localhost',
    db='test')

#カーソルを取得する
cur = conn.cursor()

#テーブルを作成する
cur.execute('DROP TABLE IF EXISTS items')
cur.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
    )
    ''')

#データを挿入する
#MySQLでは「%s」と書いた部分が実際の値と置き換わる
data = [('Banana', 300),('Mango', 640), ('Kiwi', 280)]
for i in data:
    cur.execute("INSERT INTO items(name,price) VALUES(%s,%s)", i)

#SELECT分でデータを抽出した後fetchall()メソッドで全て取得する
cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)

