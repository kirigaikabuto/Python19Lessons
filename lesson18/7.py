def Minimize(array):
    n = len(array)
    for i in range(n):
        array[i] = array[i] - 1


arr = [1, 2, 3, 4]
print(arr)  # 1,2,3,4
Minimize(arr)
print(arr)  # 0,1,2,3
