import csv, codecs

#CSVファイルを開く
filename = "list-sjis.csv"
fp = codecs.open(filename, "r", "shift_jis")

#1行ずつ読む
reader = csv.reader(fp, delimiter=",", quotechar='"') #delimiter(区切り文字) quotechar(どの記号でデータを囲むか)
for cells in reader:
    print(cells[1], cells[2])