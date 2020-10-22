arr = [
    [1, 2, 3, 4],
    [11, 5, 6, 12],
    [7, 8, 9, 10]
]
num = int(input())  # 8 -> [2,1]
i = 0
n = len(arr)
while i < n:
    subArray = arr[i]
    j = 0
    k = len(subArray)
    while j < k:
        if subArray[j] == num:
            print(i, j)
            break
        j += 1
    i += 1
