from janome.tokenizer import Tokenizer
import zipfile
import os.path, urllib.request as req

#銀河鉄道の夜のZIPファイルをダウンロード
url = "http://www.aozora.gr.jp/cards/000081/files/456_ruby_145.zip"
local = "456_ruby_145.zip"
if not os.path.exists(local):
    print("ZIPファイルをダウンロード")
    req.urlretrieve(url, local)

#ZIPファイル内のテキストファイルを読む
zf = zipfile.ZipFile(local, 'r') #zipファイルを読む
fp= zf.open('gingatetsudono_yoru.txt', 'r') #アーカイブ内のテキストを読む
bindata = fp.read()
txt = bindata.decode('shift_jis') #テキストがShift_JISなのでデコード

#形態素解析オブジェクトの生成
t = Tokenizer()

#テキストを一行ずつ処理
word_dic = {}
lines = txt.split("\r\n")
for line in lines:
    malist = t.tokenize(line)
    for w in malist:
        word = w.surface #surfaceが単語を得る
        ps = w.part_of_speech #part_of_speechが品詞情報を得る

        if ps.find('名詞') < 0: continue #名詞だけカウントしたいのでそれ以外は抜ける

        if not word in word_dic: #word_dicにwordが含まれていない場合
            word_dic[word] = 0
        word_dic[word] += 1 #カウント

#よく使われる単語を表示
#出現頻度順に並び替える
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word,cnt in keys[:50]:
    print("{0}({1}) ".format(word,cnt), end="")

