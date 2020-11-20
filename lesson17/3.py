import json

file = open("testData.json", "r")
data = file.read()
jsonData = json.loads(data)
print(jsonData)
