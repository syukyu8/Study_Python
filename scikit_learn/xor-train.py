from sklearn import svm

#XORの演算結果
xor_data = [
    #P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

#学習させるためにデータとラベルに分ける
#fit()の仕様に合わせるため
data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])
    label.append(r)

#SVMを用いてデータの学習
clf = svm.SVC()
#fit(学習するデータの配列, 正解ラベルの配列)
clf.fit(data, label)

#データを予測
pre = clf.predict(data)
print("予測結果:", pre)

#正解と合っているか結果を確認
ok = 0; total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer: ok += 1
    total += 1
print("正解率:", ok, "/", total, "=", ok/total)