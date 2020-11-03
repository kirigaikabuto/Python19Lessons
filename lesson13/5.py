n = 5
all = []
for i in range(n):
    arr = []
    for j in range(n):
        arr.append(0)
    all.append(arr)

points = [
    [0, 0],
    [3, 4],
    [4, 3],
    [1, 3]
]

for point in points:
    x, y = point  # [3,4] -> x=3,y=4
    all[x][y] = 1
for i in all:
    print(i)
# [1, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 1]
# [0, 0, 0, 1, 0]
