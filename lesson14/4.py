# b = {
#     "name": "teacher1",
#     "subject": "math",
#     "salary": 1000,
#     "age": 50
# }
# keys = []
# values = []
# for i in b:
#     keys.append(i)
#     values.append(b[i])
# print(keys)
# print(values)

d = {}
keys = ['name', 'subject', 'salary', 'age']
values = ['teacher1', 'math', 1000, 50]
# code
n = len(keys)
# i = 0
# while i < n:
#     d[keys[i]] = values[i]
#     i += 1
for i in range(n):
    d[keys[i]] = values[i]
print(d)  # {'name': 'teacher1', 'subject': 'math', 'salary': 1000, 'age': 50}

# teacher2 = {
#     "name": "teacher2",
#     "subject": "history",
#     "salary": 3000,
# }
# teacher3 = {
#     "name": "teacher3",
#     "subject": "math",
#     "salary": 2000,
#     "age": 30
# }
