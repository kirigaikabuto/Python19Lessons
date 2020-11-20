import json

# read data
filename = "users.json"
file = open(filename, "r")
dataJson = file.read()
users = json.loads(dataJson)
# create new data
username = input("username:")
password = input("password:")

user = {
    "username": username,
    "password": password
}
users.append(user)
# save data
fileWrite = open(filename, "w")
dataJson = json.dumps(users, indent=4)
fileWrite.write(dataJson)
fileWrite.close()
