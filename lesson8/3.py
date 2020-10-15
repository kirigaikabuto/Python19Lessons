# 3
# 123
# 432
# 545
# arr = [123, 432, 545]
n = int(input("count of element in array:"))
i = 0
arr = []
while i < n:
    num = int(input("element:"))
    arr.append(num)
    i += 1
i = 0
sumi = 0
while i < n:
    sumi = sumi + arr[i]
    i += 1
print(sumi)
