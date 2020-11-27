import json
from dictSupport import *

users = getDataFromJsonFile("users.json")
user = {
    "name": "user4",
    "salary": 10000,
    "age": 123
}
users.append(user)
saveDataToJsonFile("users.json", users)
