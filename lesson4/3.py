# 1)найти среднее число
# пример 1:
# 3
# 1
# 2
# среднее число:2
#
# пример 2:
# 4
# 3
# 0
# среднее число:3
a = int(input())
b = int(input())
c = int(input())
maxi = 0
mini = 0
middle = 0
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
#find middle
if a != maxi and a != mini:
    middle = a
if b != maxi and b != mini:
    middle = b
if c != maxi and c != mini:
    middle = c
print(f"Максимальное число {maxi}")
print(f"Минимальное число {mini}")
print(f"Среднее число {middle}")
