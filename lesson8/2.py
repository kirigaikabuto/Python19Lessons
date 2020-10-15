arr = []
arr2 = []
initial = 1
end = 100
while initial <= end:
    arr.append(initial)
    initial += 1
# code
i = 0
n = len(arr)
while i < n:
    #i -> индекс
    #arr[i]-> это значение массива под этим индексом
    if arr[i] % 2 == 0:
        arr2.append(arr[i])
    i += 1
print(arr2)
