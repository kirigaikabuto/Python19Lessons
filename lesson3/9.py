# x,y
# x=3
# y=4
# 0 <= x <=10 -> значение подходит
# иначе вывести что это не подходит
# 0 <= x <=10
# x>=0
# x<=10
# and -> и
# or -> или
# y==10 или y=25
x = int(input("x="))
y = int(input("y="))
#and -> условие1 == true,условие2==true
#or -> условие1 == true,условие2==false
#or -> условие1 == false,условие2==true
#or ->условие1 == true,условие2==true

if x >= 0 and x <= 10:
    print("x подходит")
else:
    print("x не подходит")

if y == 10 or y == 25:
    print("y подходит")
else:
    print("y не подходит")
#задача
первое число:3
второе число:4
третье число:5
5
a = int(input("первое число:"))
b = int(input("второе число:"))
c = int(input("третье число:"))


# if y == 10:
#     print("y подходит")
# else:
#     print("y не подходит")
#
# if y == 25:
#     print("y подходит")
# else:
#     print("y не подходит")