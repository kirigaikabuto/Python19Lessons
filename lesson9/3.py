n = int(input())
i = 0
arr = []
arr2 = []
while i < n:
    num = int(input())
    arr.append(num)
    i += 1
i = 0
sumi = 0
while i < n:
    sumi = sumi + arr[i]
    i += 1
average = sumi / n
i = 0
while i < n:
    if arr[i] < average:
        arr2.append(arr[i])
    i += 1
print(arr2)
