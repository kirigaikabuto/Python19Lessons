import json
user1 = {
    "username": "admin1",
    "password": "passanya1",
}
data = json.dumps(user1)
# json.dumps - >он превращает словарь в json
file = open("data.json", "w")
file.write(data)
file.close()
