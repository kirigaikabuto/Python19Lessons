a = int(input())#1
b = int(input())#5
c = int(input())#2
d = int(input())#4
#1 5
sumi = 0
while a <= b:
    if a < c or a > d:
        sumi += a
    a += 1
print(sumi)
# 10
# 20
# 12
# 15
#
# 12 13 14 15
#
# 10+11+16+17+18+19+20
