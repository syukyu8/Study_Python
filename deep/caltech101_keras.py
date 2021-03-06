from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPool2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np

#カテゴリの指定
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)
#画像サイズを指定
image_w = 64 
image_h = 64

#データをロード
X_train, X_test, y_train, y_test = np.load("./image/5obj.npy", allow_pickle=True) #自分で作ったファイルならTrueにして良い
#データを正規化する
X_train = X_train.astype("float") / 256
X_test  = X_test.astype("float")  / 256
print('X_train shape:', X_train.shape)

#モデルを構築
in_shape = X_train.shape[1:]
model = Sequential()
model.add(Conv2D(32, 3, input_shape=in_shape)) #入力データ形式を指定する
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes)) #出力データのカテゴリー数を指定する
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy'])

#モデルを訓練する
model.fit(X_train, y_train, batch_size=32, epochs=50)

#モデルを評価する
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])