#色々参考書通りになるよう試したけどうまくいかなかったので結局公式チュートリアル通りにやりました
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
# from keras.models import Sequential
# from keras.layers.core import Dense, Dropout, Activation
# from keras.optimizers import Adam 
# from keras.utils import np_utils

#MNISTのデータを読み込む
(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()

#ピクセルの値を0~1の間に正規化
#配布データは各ピクセルの色の濃さを0~255までの8ビットで表現しているため
X_train = X_train.reshape((60000, 28, 28, 1))
X_test  = X_test.reshape((10000, 28, 28, 1))
X_train = X_train / 255.0
X_test  = X_test / 255.0

#モデルの構造を定義
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# model.add(Dense(512, input_shape=(784,)))
# model.add(Activation('relu'))
# model.add(Dropout(0.2))

# model.add(Dense(512))
# model.add(Activation('relu'))
# model.add(Dropout(0.2))

# model.add(Dense(10))
# model.add(Activation('softmax'))

#モデルを構築
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])


#データで訓練
hist = model.fit(X_train, y_train)

# テストデータを用いて評価する
score = model.evaluate(X_test, y_test, verbose=1)
print('loss=', score[0])
print('accuracy=', score[1])