#from sklearn import cross_validation
import sklearn.model_selection as cross_validation
from PIL import Image
import os, glob
import numpy as np

#分類対象のカテゴリを選ぶ
caltech_dir = "./image/101_ObjectCategories"
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)

#画像サイズを指定
image_w = 64 
image_h = 64
pixels = image_w * image_h * 3 #各ピクセルごとにRGBの3個のデータが必要なので3*64*64

#画像データを読み込み
X = [] #実際の画像データ
Y = [] #ラベルデータ
for idx, cat in enumerate(categories):
    #ラベルを指定
    label = [0 for i in range(nb_classes)]
    label[idx] = 1
    #画像ファイルを列挙する
    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir+"/*.jpg") #jpgのものだけ
    for i, f in enumerate(files):
        img = Image.open(f) 
        img = img.convert("RGB") #色モードをRGBに変換
        img = img.resize((image_w, image_h)) #Numpyの配列データに変換
        data = np.asarray(img)
        X.append(data)
        Y.append(label)
        if i % 10 == 0:
            print(i, "\n", data)
X = np.array(X)
Y = np.array(Y)

#学習データとテストデータを分ける
X_train, X_test, y_train, y_test = \
    cross_validation.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./image/5obj.npy", xy)

print("ok,", len(Y))