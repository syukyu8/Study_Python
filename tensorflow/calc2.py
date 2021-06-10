#TensorFlowを取り込む
import tensorflow as tf

#定数を定義
a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

#演算を定義
calc1_op = a + b * c
calc2_op = (a + b) * c

#結果を表示する
tf.print(calc1_op)
tf.print(calc2_op)
