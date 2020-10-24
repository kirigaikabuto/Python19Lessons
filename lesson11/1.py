arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
num = int(input())
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
