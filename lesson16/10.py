import json

arr = [
    {"name": "123"},
    {"name": "456"}
]
file = open("data.json", "w")
dataJson = json.dumps(arr, indent=4)
file.write(dataJson)
file.close()
