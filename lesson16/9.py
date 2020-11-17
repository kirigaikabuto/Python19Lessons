import json

file = open("data.json", "r")
data = file.read()
d = json.loads(data)
print(d["username"])
# словарь -> json json.dumps()
# словарь -> json -> записали в файл data.json -> словарь
# считываем все данные из data.json-> json -> словарь
# json -> словарь json.loads()
