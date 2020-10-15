# вводятся какое определенное колво чисел n, и среди них необходимо найти
# среднее ариф число
# 3
# 4
# 5
# 6
#
# 5
n = int(input())
i = 0
arr = []
while i < n:
    num = int(input())
    arr.append(num)
    i += 1
i = 0
sumi = 0
while i < n:
    sumi = sumi + arr[i]
    i += 1
print(sumi/n)
