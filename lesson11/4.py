n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
sumi = 0
for i in arr:
    sumi = sumi + i
print(sumi // n)
