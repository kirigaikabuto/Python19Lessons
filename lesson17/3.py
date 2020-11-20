import json

ingredient1 = {
    "id": 1,
    "name": "tomato",
}
ingredient2 = {
    "id": 2,
    "name": "cheese",
}
ingredient3 = {
    "id": 3,
    "name": "garlic"
}
ingredients1 = [ingredient1, ingredient2]
pizza1 = {
    "id": 1,
    "title": "Primavera Pizza",
    "price": 3.99,
    "ingredients": ingredients1
}
ingredients2 = [ingredient1, ingredient3]
pizza2 = {
    "id": 2,
    "title": "Vegetarian Pizza",
    "price": 5.99,
    "ingredients": ingredients2
}
pizzas = [pizza1, pizza1]
# file write
filename = "pizzas.json"
file = open(filename, "w")
dataJson = json.dumps(pizzas, indent=4)
file.write(dataJson)
file.close()
