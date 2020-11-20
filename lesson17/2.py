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
# check for existing
k = 0
for i in users:
    if i["username"] == user["username"]:
        k = 1

if k == 0:
    users.append(user)
    # save data
    fileWrite = open(filename, "w")
    dataJson = json.dumps(users, indent=4)
    fileWrite.write(dataJson)
    fileWrite.close()
else:
    print("User with that username already exist")
