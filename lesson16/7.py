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
username = input("username:")
password = input("password:")
if username == "" or password == "":
    print("заполните все данные")
else:
    k = 0
    for i in users:
        if i["username"] == username:
            person = i
            k = 1
    if k == 1:
        print("у нас уже есть такой пользователь")
    else:
        user = {
            "username": username,
            "password": password,
        }
        users.append(user)
print(users)
