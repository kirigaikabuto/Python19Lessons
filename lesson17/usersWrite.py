import json

user1 = {
    "username": "username1",
    "password": "password1",
}
user2 = {
    "username": "username2",
    "password": "password2",
}
user3 = {
    "username": "username3",
    "password": "password3",
}
users = [user1, user2, user3]
filename = "users.json"
file = open(filename, "w")
dataJson = json.dumps(users, indent=4)
file.write(dataJson)
file.close()
