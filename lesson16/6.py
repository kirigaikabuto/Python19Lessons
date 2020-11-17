user1 = {
    "username": "admin1",
    "password": "passanya1",
}
user2 = {
    "username": "admin2",
    "password": "passanya2",
}
user3 = {
    "username": "admin3",
    "password": "passanya3",
}
users = [user1, user2, user3]
username = input()
password = input()
k = 0
person = {}
for i in users:
    if i["username"] == username and i["password"] == password:
        person = i
        k = 1

if k == 1:
    print("you have access", person["username"])
else:
    print("no user")
