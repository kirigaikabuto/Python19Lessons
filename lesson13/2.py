import random

arr = []
n = int(input("count of element in array:"))
for i in range(n):
    k = random.randint(1, 100)
    arr.append(k)

#
# 5
# [
#     [1,0,-1,12,3],
#     [34,12,23,23,1],
#     [43,123,32,3,4],
#     [43,123,32,5,6],
#      [43,123,32,5,],
# ]
# i = 0
# while i < n:
#     k = random.randint(10, 20)
#     arr.append(k)
#     i += 1
print(arr)
