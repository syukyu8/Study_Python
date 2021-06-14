import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import pandas as pd, numpy as np

#BMIのデータを読み込んで正規化する
csv = pd.read_csv("bmi.csv")
#体重と身長のデータを0~1になるように正規化する
csv["weight"] /= 100
csv["height"] /= 200
X = csv[["weight", "height"]] #PandasでCSVファイルを読み込んで任意列を抽出する方法
#ラベル
bclass = {"thin":[1,0,0], "normal":[0,1,0], "fat":[0,0,1]}
y = np.empty((20000,3))
for i, v in enumerate(csv["label"]):
    y[i] = bclass[v]
#訓練データとテストデータを分ける
X_train, y_train = X[1:15001], y[1:15001]
X_test,  y_test  = X[15001:20001], y[15001:20001] 


#モデルの構造を定義
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(2,)))
model.add(layers.Dropout(0.1))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.1))
model.add(layers.Dense(3, activation='softmax'))

#モデルを構築
model.compile(
    loss='categorical_crossentropy',#sparseを付けるとShape mismatchになります
    #https://stackoverflow.com/questions/58398491/valueerror-shape-mismatch-the-shape-of-labels-received-15-should-equal-th
    optimizer="rmsprop",
    metrics=['accuracy'])

#データで訓練
callbacks = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=2)#データの精度が減少した時訓練を中止してくれる
hist = model.fit(
    X_train, y_train,
    batch_size=100,
    epochs=20,
    validation_split=0.1,
    callbacks=[callbacks],
    verbose=1)

#テストデータを用いて評価する
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])