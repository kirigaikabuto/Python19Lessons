import json

user1 = {
    "name": "user1",
    "salary": 1230,
    "age": 20,
}
user2 = {
    "name": "user2",
    "salary": 2230,
    "age": 12,
}
user3 = {
    "name": "user3",
    "salary": 1000,
    "age": 33,
}
users = [user1, user2, user3]
usersJson = json.dumps(users, indent=4)
file = open("users.json", "w")
file.write(usersJson)
file.close()
