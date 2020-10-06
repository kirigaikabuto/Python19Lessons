arr = [1, 2, 3, 12323, 4, 5, 432, 6, 7, 8, 9, 10]
sumi = 0
i = 0
n = len(arr)  # колво элементов в массиве 12
#0 1 2 3 4 5 6 7 8 9 10 11
#arr[12]->error
while i <= n:
    sumi = sumi + arr[i]
    i += 1
print(sumi)
# i=0, arr[0] ->1
# i=1, arr[1] ->2
# i=2, arr[2] ->3
# 36
