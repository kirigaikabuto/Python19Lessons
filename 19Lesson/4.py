from dictSupport import *
import json

file = open("users.json", "r")
dataJson = file.read()
users = json.loads(dataJson)
print(users)
printData(users)
