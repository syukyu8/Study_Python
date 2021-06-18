#レーベシュタイン距離を求める 2つの文字列がどの程度異なっているか示すもの
def calc_distance(a, b):
    ''' レーベンシュタイン距離を計算する '''
    if a == b: return 0
    a_len = len(a)
    b_len = len(b)
    if a == "": return b_len
    if b == "": return a_len
    #二次元の表(a_len+1, b_len+1)を準備
    #比較する文字列aとbの長さ+1のサイズを持つ
    matrix = [[] for i in range(a_len+1)]
    for i in range(a_len+1): #0で初期化
        matrix[i] = [0 for j in range(b_len+1)]
    #0の時の初期値を設定
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
    #表を埋める
    #左上から右下へと順に埋める
    #i文字目とj文字目について最小コストとなる編集を求めて表を埋める
    for i in range(1, a_len+1):
        ac = a[i-1]
        for j in range(1, b_len+1):
            bc = b[j-1]
            cost = 0 if (ac == bc) else 1
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     #文字の挿入
                matrix[i][j-1] + 1,     #文字の削除
                matrix[i-1][j-1] + cost #文字の置換
            ])
    return matrix[a_len][b_len]

#カキトメとカンヅメの距離は？
print(calc_distance("カキトメ", "カンヅメ"))

#実行例
samples = ["イカダ", "イカスミ", "イカ", "サカナ", "サンマ", "カナダ"]
base = samples[0]
r = sorted(samples,
    key = lambda n: calc_distance(base, n))
for n in r:
    print(calc_distance(base, n), n)