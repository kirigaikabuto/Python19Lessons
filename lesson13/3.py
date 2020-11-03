import random

n = int(input())
all = []
for i in range(n):
    arr = []
    for j in range(n):
        k = random.randint(1, 100)
        arr.append(k)
    all.append(arr)
print(all)
