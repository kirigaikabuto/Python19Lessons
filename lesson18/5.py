def printSum(array):
    sumi = 0
    for i in array:
        sumi = sumi + i
    print(sumi)


def printMax(arr):
    maxi = arr[0]
    for i in arr:
        if i > maxi:
            maxi = i
    print(maxi)


arr0 = [1, 2, 3, 4, ]
arr1 = [1, 2, 2, 3, ]
arr2 = [1, 3, 2, 4, ]
printMax(arr0)
printMax(arr1)
printMax(arr2)
# printSum(arr0)
# printSum(arr1)
# printSum(arr2)
