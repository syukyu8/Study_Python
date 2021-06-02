import json

price = {
    "data": "2020-05-10",
    "price": {
        "Apple":80,
        "Orange":55,
        "Banana":40
    }
}

s = json.dumps(price)
#キーの順番は順不同
print(s)