import sqlite3

#sqliteのデータベースに接続
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

#テーブルを作成し、データを挿入する
cur = conn.cursor()
#1文ずつ実行する場合はexecutescript()ではなくexcute()メソッドが使える
cur.executescript("""
/* itemsテーブルが既にあれば削除する */
DROP TABLE IF EXISTS items;

/* テーブルの作成 */
CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

/* データを挿入  */
INSERT INTO items(name, price)VALUES('Apple', 800);
INSERT INTO items(name, price)VALUES('Orange', 780);
INSERT INTO items(name, price)VALUES('Banana', 430);
""")
#上記の操作をデータベースに反映させる
conn.commit()

#データを抽出する
cur = conn.cursor()
cur.execute("SELECT item_id,name,price FROM items")

#fetchall()メソッドで結果を全て取得できる
#1つだけ取得したい時はfetchone()メソッドを使う
item_list = cur.fetchall()

#一行ずつ表示
for it in item_list:
    print(it)
