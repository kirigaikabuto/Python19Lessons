a = int(input())  # 9
b = int(input())  # 15
# 9 10 11 12 13 14 15
sumi = 0
while a <= b:
    if a % 2 == 0:
        sumi = sumi + a
    a += 1
print(sumi)
# if a%2 == 0:
#     print("yes")
# else:
#     print("no")
