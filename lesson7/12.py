# 10 30
# 10 + 13 + 16 + 19 + 21 + 24....
# 10 11 12 13
a = int(input())
b = int(input())
sumi = 0
while a <= b:
    sumi = sumi + a
    a += 3

# sumi=10+3
# sumo=13+11+3
print(sumi)
