def printData(arr123213):
    for i in arr123213:
        marks = i["marks"]
        avg = 0
        for j in marks:
            avg = avg + j
        print(i["name"], avg / len(marks))


user1 = {
    "name": "user1",
    "marks": [1, 2, 3, 4, 5]
}
user2 = {
    "name": "user2",
    "marks": [4, 2, 3, 3, 5]
}
user3 = {
    "name": "user3",
    "marks": [4, 2, 3, 3, 5]
}
students = [user1, user2]
students2 = [user1, user3]
printData(students)
printData(students2)
