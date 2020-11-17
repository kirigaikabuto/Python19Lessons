import random
a = {
    "name": "name1"
}
b = {
    "name": "name2"
}
c = {
    "name": "name3"
}
arr = [a, b, c]
print(arr)
for el in arr:
    el["age"] = random.randint(1, 20)
print(arr)
