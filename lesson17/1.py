import json

filename = "users.json"
file = open(filename, "r")
dataJson = file.read()
users = json.loads(dataJson)
username = input("username:")
password = input("password:")
k = 0
for user in users:
    if user["username"] == username and user["password"] == password:
        k = 1

if k == 1:
    print("ok")
else:
    print("user not found")
