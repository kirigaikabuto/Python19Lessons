def printArrElements(array):
    for i in array:
        print(i)


def printArrElementAndIndex(array):
    n = len(array)
    for i in range(n):
        print(i, array[i])


def getMax(a):
    maxi = a[0]
    for i in a:
        if i > maxi:
            maxi = i
    return maxi
