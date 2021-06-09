import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

#アヤメのCSVデータを読み込む
csv = pd.read_csv('iris.csv')

#リストを訓練データとラベルに分割する
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

#クロスバリデーションを行う
#ライブラリ使えば数行で書ける
clf = svm.SVC()
#model_selection.cross_val_score(学習評価器のオブジェクト, 訓練データ, 正解ラベル, 何分割するか)
#numpy.ndarrayが返ってくるので平均計算させるだけ
scores = model_selection.cross_val_score(
	clf, data, label, cv=5)
print("各正解率=", scores)
print("正解率=", scores.mean())
