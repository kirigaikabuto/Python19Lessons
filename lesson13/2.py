import random

arr = []
n = int(input("count of element in array:"))
for i in range(n):
    k = random.randint(10, 20)
    arr.append(k)

#
# 3
# [
#     [1,0,-1],
#     [34,12,23],
#     [43,123,32],
# ]
# i = 0
# while i < n:
#     k = random.randint(10, 20)
#     arr.append(k)
#     i += 1
print(arr)
