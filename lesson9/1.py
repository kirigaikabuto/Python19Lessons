# 3)
# # дается n чисел и необходимо найти среди них те числа
# # которые делятся на k без отстатка и
# # поместить их в другой массив
#
# # 5               n
# # 10
# # 16
# # 15
# # 30
# # 41
# # 5               k
# #
# # Ответ:[10,15,30]
n = int(input())
i = 0
arr = []
arr2 = []
while i < n:
    num = int(input())
    arr.append(num)
    i += 1
k = int(input())
i = 0
while i < n:
    if arr[i] % k == 0:
        arr2.append(arr[i])
    i += 1
print(arr2)
