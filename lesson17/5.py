import json

file = open("pizzas.json", "r")
dataJson = file.read()
pizzas = json.loads(dataJson)
sumi = 0
for i in pizzas:
    sumi = sumi + i["price"]
n = len(pizzas)
print(sumi)
avg = sumi / n
print(avg)
