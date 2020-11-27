import json
from dictSupport import *


def readFromJsonFile(fileName):
    file = open(fileName, "r")
    dataJson = file.read()
    data = json.loads(dataJson)
    return data


def saveToJsonFile(fileName, data):
    dataJson = json.dumps(data, indent=4)
    file = open(fileName, "w")
    file.write(dataJson)
    file.close()


users = readFromJsonFile("users.json")
user = {
    "name": "user4",
    "salary": 10000,
    "age": 123
}
users.append(user)
saveToJsonFile("users.json", users)
