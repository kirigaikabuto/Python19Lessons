import json
from dictSupport import *





users = readFromJsonFile("users.json")
user = {
    "name": "user4",
    "salary": 10000,
    "age": 123
}
users.append(user)
saveToJsonFile("users.json", users)
