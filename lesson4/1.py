# 1)
# ВВОД:
#
# первое число:3
# второе число:4
# третье число:5
#
# ВЫВОД:
# Максимальное число:5
# Минимальное число:3
a = int(input())
b = int(input())
c = int(input())
maxi = 0
mini = 0
#find maximum
if a > b and a > c:
    maxi = a

if b > a and b > c:
    maxi = b

if c > a and c > b:
    maxi = c
#find minimum
if a < b and a < c:
    mini = a

if b < a and b < c:
    mini = b

if c < a and c < b:
    mini = c
print(f"Максимальное число {maxi}")
print(f"Минимальное число {mini}")