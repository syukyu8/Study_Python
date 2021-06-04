import sqlite3

#データベースに接続
filepath = "test2.sqlite"
conn = sqlite3.connect(filepath)

#テーブルを作成
#1文ずつ実行する時はexecute()メソッド
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items") 
cur.execute(""" CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    name    TEXT,
    price   INTEGER)""")
conn.commit()

#単発でデータを挿入
#SQL内で実際に挿入する値は「?」を使って表現
#第2引数に実際の値を指定する
#文字列なら自動的にクォート処理
#クォートがあった場合自動的にエスケープしてくれる
cur = conn.cursor()
cur.execute(
    "INSERT INTO items (name,price) VALUES (?,?)",
    ("Orange", 520))
conn.commit()

#連続でデータを挿入
cur = conn.cursor()
data = [("Mango",770), ("Kiwi",400), ("Grape",800),
    ("Peach",940),("Persimmon",700),("Banana", 400)]
cur.executemany(
    "INSERT INTO items(name,price) VALUES (?,?)",
    data)
conn.commit()

#400-700円のデータを抽出して表示
#タプルに値を1つだけ指定したい時は(400,)と書けばいいらしい
cur = conn.cursor()
price_range = (400, 700)
cur.execute(
    "SELECT * FROM items WHERE price>=? AND price<=?",
    price_range)
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)

