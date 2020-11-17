import json

file = open("data.json", "r")
dataJson = file.read()
arr = json.loads(dataJson)
for i in arr:
    print(i["name"])
