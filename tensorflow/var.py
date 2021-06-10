import tensorflow as tf

#定数を定義(名前付き引数で変数名を明示できる)
a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")
#変数を定義
v = tf.Variable(0, name="v")

#データフローグラフを定義
#tensorflow2.0ではtf.assign()も無くなったらしい
v = a + b + c

#vの内容を表示する
tf.print(v)