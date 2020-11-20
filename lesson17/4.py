import json

file = open("pizzas.json", "r")
dataJson = file.read()
pizzas = json.loads(dataJson)
for pizza in pizzas:
    ingredients = pizza["ingredients"]
    for i in ingredients:
        print(i["name"])
