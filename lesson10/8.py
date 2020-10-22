arr = [
    [1, 9, 3],
    [4, 0, 6],
    [8, 9, 10],
]
i = 0
n = len(arr)
while i < n:
    subArray = arr[i]
    j = 0
    k = len(subArray)
    maxi = subArray[0]
    while j < k:
        if maxi < subArray[j]:
            maxi = subArray[j]
        j += 1
    print(maxi)
    i += 1
# 1 9 3
# 4 0 6
# 8 9 10
#
# 9
# 6
# 10
