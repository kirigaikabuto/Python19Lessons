# 1
# 20
first = int(input())
second = int(input())
i = first
arr = []
while i <= second:
    if i % 2 != 0:
        arr.append(i)
    i += 1
# code добавление нечетных элементов
print(arr)
