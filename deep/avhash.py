from PIL import Image
import numpy as np

#画像データをAverage Hashに変換
def average_hash(fname, size = 16):
    img = Image.open(fname) #画像データを開く
    img = img.convert('L') #「L」を指定するとグレースケールに変換　「1」を指定すると二値化
    img = img.resize((size, size), Image.ANTIALIAS) #リサイズ
    pixel_data = img.getdata() #画像のピクセルデータを得る
    pixels = np.array(pixel_data) #Numpyの配列に変換
    pixels = pixels.reshape((size, size)) #二次元の配列に変換
    avg = pixels.mean() #算術平均を計算
    diff = 1 * (pixels > avg) #平均より上なら1、下なら0
    return diff

#二進数とみなしてハッシュ値に変換
def np2hash(n):
    bhash = []
    for nl in ahash.tolist():
        sl = [str(i) for i in nl]
        s2 = "".join(sl)
        i = int(s2, 2) #二進数を16進数のハッシュ値に変換する
        bhash.append("%04x" % i)
    return "".join(bhash)


#Average Hashを表示
ahash = average_hash('tower.jpg')
print(ahash)
print(np2hash(ahash))