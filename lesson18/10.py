def getMax(arr):
    maxi = arr[0]
    for i in arr:
        if i > maxi:
            maxi = i
    return maxi


arr1 = [1, 2, 3, 4]
arr2 = [4, 5, 6, 7, 8]
maxi1 = getMax(arr1)
maxi2 = getMax(arr2)
print(maxi1 + maxi2)
