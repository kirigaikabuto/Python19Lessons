arr = [1, 2, 3, 4]
i = 0
n = len(arr)
sumi = 0
maxi = arr[0]
while i < n:
    sumi = sumi + arr[i]
    if maxi < arr[i]:
        maxi = arr[i]
    i += 1
