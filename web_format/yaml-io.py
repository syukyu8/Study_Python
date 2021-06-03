import yaml

#PythonのデータをYAMLで出力
customer = [
    { "name": "Yamada", "age": "35", "gender": "man" },
    { "name": "Sato",   "age": "58", "gender": "woman" },
    { "name": "Kato",   "age": "42", "gender": "man" },
    { "name": "Nishi",  "age": "22", "gender": "man" }
]

#PythonのデータをYAMLに変換
yaml_str = yaml.dump(customer)
print(yaml_str)
print("--- --- ---")

#YAMLをPythonデータに変換
data = yaml.load(yaml_str, Loader=yaml.SafeLoader)

#顧客名だけ表示
for p in data:
    print(p["name"])