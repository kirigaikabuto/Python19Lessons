def getMax(arr):
    maxi = arr[0]
    for i in arr:
        if i > maxi:
            maxi = i
    return maxi


def getSum(arr):
    sumi = 0
    for i in arr:
        sumi += i
    return sumi
