arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = []
element = 11
while element <= 100:
    arr1.append(element)
    element += 1

j = 0
# len() количество элементов в массиве
end = len(arr1)
while j < end:
    if arr1[j] % 2 == 0:
        arr2.append(arr1[j])
    j += 1
print(arr1)