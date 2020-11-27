def printUsers(data):
    for i in data:
        print(i["name"], i["salary"])


def getUserWithMaxSalary(data):
    maxiUser = data[0]
    for i in data:
        if i["salary"] > maxiUser["salary"]:
            maxiUser = i
    return maxiUser


def getUserWithMaxAge(data):
    maxiUser = data[0]
    for i in data:
        if i["age"] > maxiUser["age"]:
            maxiUser = i
    return maxiUser


user1 = {
    "name": "user1",
    "salary": 1230,
    "age": 20,
}
user2 = {
    "name": "user2",
    "salary": 2230,
    "age": 12,
}
user3 = {
    "name": "user3",
    "salary": 1000,
    "age": 33,
}
users = [user1, user2, user3]
printUsers(data=users)
output = getUserWithMaxSalary(data=users)
maxiAge = getUserWithMaxAge(data=users)
print(maxiAge)
