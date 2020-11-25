from utils import getMax, getSum

arr1 = [1, 2, 3, 4]
arr2 = [4, 5, 6, 7, 8]
arr3 = [1312313, 3443, 43123213]
arr4 = [12, 3, 2, 1323]
arrays = [arr1, arr2, arr3, arr4]
for i in arrays:
    maxi = getMax(i)
    sumi = getSum(i)
    print(i, maxi, sumi)
