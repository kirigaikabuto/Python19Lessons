teacher1 = {
    "name": "teacher1",
    "subject": "math",
    "salary": 1000,
    "age": 50
}
teacher2 = {
    "name": "teacher2",
    "subject": "history",
    "salary": 3000,
}
teacher3 = {
    "name": "teacher3",
    "subject": "math",
    "salary": 2000,
    "age": 30
}
#если это учитель math и его возраст 40 < age < 60 -> 30%
#если это учитель math и его возраст 25 < age < 40 -> 20%
if teacher1["subject"] == "math":
    teacher1["salary"] = teacher1["salary"] + teacher1["salary"] * 0.1
if teacher2["subject"] == "math":
    teacher2["salary"] = teacher2["salary"] + teacher2["salary"] * 0.1
if teacher3["subject"] == "math":
    teacher3["salary"] = teacher3["salary"] + teacher3["salary"] * 0.1
print(teacher1)
print(teacher2)
print(teacher3)
