# 1) найти вывести имя самого взрослого и самого маленького из массива
arr = [
    {
        "name": "yerassyl1",
        "age": 23,
    },
    {
        "name": "yerassyl2",
        "age": 3,
    },
    {
        "name": "yerassyl3",
        "age": 43,
    },
    {
        "name": "yerassyl4",
        "age": 123,
    }
]
maxi = arr[0]["age"]
person = {}
for i in arr:
    if i["age"] > maxi:
        maxi = i["age"]
        person = i
print(person)
