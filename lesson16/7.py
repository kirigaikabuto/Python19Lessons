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
#code
# введите username:admin123
# введите password:admin123

print(users)
# otvet
# [{'username': 'admin1', 'password': 'passanya1'},
# {'username': 'admin2', 'password': 'passanya2'},
# {'username': 'admin3', 'password': 'passanya3'},
# {'username': "admin123","password":"admin123"},
# ]
