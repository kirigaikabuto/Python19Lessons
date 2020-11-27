from dictSupport import *

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
output = getMaxDataByParam(data=users, param="salary")
maxiAge = getMaxDataByParam(data=users, param="age")
allSalary = getParamSum(data=users, param="salary")
print(maxiAge)
print(output)
print(allSalary)
