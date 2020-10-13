a = int(input())  # 9
b = int(input())  # 15
# 9 10 11 12 13 14 15
#3  10
# # while <=10
# #   if %2 == 0:
#         ...

sumi = 0
while a <= b:
    if a % 2 == 0:
        print(a,"in if")
        sumi = sumi + a
    print(a,"out of if")
    a += 1
print(sumi)


# if a%2 == 0:
#     print("yes")
# else:
#     print("no")
