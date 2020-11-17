a = {
    "name": "yerassyl",
    "age": 16,
    "salary": 2000,
    "experience": 2,
}
b = {
    "name": "kirito",
    "age": 18,
    "salary": 3000,
    "experience": 3,
}
c = {
    "name": "lasdlsd",
    "age": 22,
    "salary": 400,
    "experience": 4,
}
peoples = [a, b, c]
for person in peoples:
    print(person["name"], person["salary"], person["age"])
sumi = 0
n = len(peoples)
for person in peoples:
    sumi = sumi + person["salary"]
print(sumi / n)
