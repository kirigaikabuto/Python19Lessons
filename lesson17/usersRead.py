import json
filename = "users.json"
file = open(filename, "r")
dataJson = file.read()
users = json.loads(dataJson)
for i in users:
    print(i["username"])
