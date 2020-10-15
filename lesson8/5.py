# вводятся n чисел и необходимо найти максимальное число
n = int(input())
i = 0
arr = []
while i < n:
    num = int(input())
    arr.append(num)
    i += 1

maxi = 0
i = 0
while i < n:
    if arr[i] > maxi:
        maxi = arr[i]
    i += 1
print(f"максимальное число {maxi}")
# 4
# 5
# 6
#
# i = 0
# maxi = 0
# arr[i]->arr[0]->4
# arr[i]>maxi -> 4>0
#     maxi = arr[i]-> maxi = 4
#
# i = 1
# maxi = 4
# arr[i] -> arr[1] -> 5
# 5>4
# maxi = 5
# a = 3
# b = 4
# c = 3
# if a>b and a>c:
#     print(a)
