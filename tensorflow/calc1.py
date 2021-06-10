#TensorFlowを取り込む
import tensorflow as tf

#定数を定義
a = tf.constant(1234)
b = tf.constant(5000)

#演算を定義
add_op = a + b

#結果を表示する
#tensorflow2.0ではSessionは使わなくて良くなったらしい
tf.print(add_op)