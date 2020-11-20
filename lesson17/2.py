import json

filename = "users.json"
file = open(filename, "r")
dataJson = file.read()
users = json.loads(dataJson)

username = input("username:")
password = input("password:")

user = {
    "username": username,
    "password": password
}
users.append(user)
fileWrite = open(filename, "w")
dataJson = json.dumps(users, indent=4)
fileWrite.write(dataJson)
fileWrite.close()
