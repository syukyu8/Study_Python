from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

#身長・体重データの読み込み
tbl = pd.read_csv("bmi.csv")

#カラム(列)をスライスして正規化
#pandasを使っているので配列全てに対して一気に計算できる
label = tbl["label"]
w = tbl["weight"] / 100 #最大100kgと考える
h = tbl["height"] / 200 #最長200cmと考える
wh = pd.concat([w, h], axis=1)

#学習用とテスト用データに分ける
data_train, data_test, label_train, label_test = \
    train_test_split(wh, label)

#データを学習
#svm.LinearSVC()にすると計算が高速になるらしい
clf = svm.SVC()
clf.fit(data_train, label_train)

#データを予測
predict = clf.predict(data_test)

#正解率を確認
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("正解率=", ac_score)
print("レポート=\n", cl_report)

