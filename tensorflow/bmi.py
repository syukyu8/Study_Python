import pandas as pd
import numpy as np
#こう書くことで2系挙動を無効化
#参考書が1.x系を想定しているので基本的にこれを書くべきかもしれない
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#身長,体重,ラベルのCSVデータを読み出す
csv = pd.read_csv("bmi.csv")
#データを正規化
csv["height"] = csv["height"] / 200
csv["weight"] = csv["weight"] / 100
#ラベルを三次元のクラスで表す
#thin=(1,0,0) / normal=(0,1,0) / fat=(0,0,1)
bclass = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x : np.array(bclass[x]))

#正解率を求めるためにテストデータを準備
test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])

#データフローグラフを構築する
x  = tf.placeholder(tf.float32, [None, 2]) #身長,体重のデータを入れる
y_ = tf.placeholder(tf.float32, [None, 3]) #答えのラベルを入れる

#変数を宣言
W = tf.Variable(tf.zeros([2, 3])); #重み
b = tf.Variable(tf.zeros([3])); #バイアス
#ソフトマックス回帰を定義
#入力xに対して、どれに分類するのが尤もらしいか表す
y = tf.nn.softmax(tf.matmul(x, W) + b)

#モデルを訓練する
#誤差関数を用いて答え合わせを行う
#誤差関数には交差エントロピーを使う
#値が小さいほど正しい値を返す
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

#下記2行で重みWやバイアスbの値を変更してくれる
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(cross_entropy)

#正解率を求める
predict = tf.equal(tf.argmax(y, 1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

# セッションを開始
sess = tf.Session()
sess.run(tf.global_variables_initializer()) #変数を初期化

#テストデータを用いて学習させる
for step in range(3500):
    i = (step * 100) % 14000
    rows = csv[1 + i : 1 + i + 100]
    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])
    fd = {x: x_pat, y_: y_ans}
    sess.run(train, feed_dict=fd)
    if step % 500 == 0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x: test_pat, y_: test_ans})
        print("step=", step, "cre=", cre, "acc=", acc)

#最終的な正解率を求める
acc = sess.run(accuracy, feed_dict={x: test_pat, y_: test_ans})
print("正解率=", acc)
        
