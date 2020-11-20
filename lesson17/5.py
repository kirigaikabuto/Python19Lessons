import json

file = open("pizzas.json", "r")
dataJson = file.read()
pizzas = json.loads(dataJson)
sumi = 0
for pizza in pizzas:
    sumi = sumi + pizza["price"]

print(sumi)
avg = sumi / n
print(avg)
