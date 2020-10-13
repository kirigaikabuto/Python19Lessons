a = int(input())
b = int(input())
c = int(input())
#a = 10
#b = 20
#c = 15
#a->10,11,12,13,14,15....
sumi = 0
while a <= b:
    if a != c:
        sumi = sumi + a
    a += 1
print(sumi)
# 10
# 15
# 13
#
# #10+11+12+14+15 =
