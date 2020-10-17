n = int(input())
i = 0
arr = []
while i < n:
    num = int(input())
    arr.append(num)
    i += 1
i = 0
sumi = 0
while i < n:
    if arr[i] % 2 == 0 and arr[i] > 0:
        sumi = sumi + arr[i]
    i += 1
print(sumi)
