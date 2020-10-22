arr = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10]
]
i = 0
n = len(arr)  # 3
while i < n:
    subArray = arr[i]  # [4, 5, 6, 7]
    j = 0
    k = len(subArray)  # 4
    sumi = 0
    print(subArray)  # [4, 5, 6, 7],
    while j < k:
        sumi = sumi + subArray[j]
        j += 1
    print(sumi)
    i += 1
