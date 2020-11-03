s = "1 2 3,4 5 6,7 8 9"
parts = s.split(",")
all = []
for i in parts:
    numbers = i.split(" ")#['1','2','3']
    temp = []
    for j in numbers:
        temp.append(int(j))#[1,2,3]
    all.append(temp)

for i in all:
    print(i)
# parts = [
#  '1 2 3',
#  '4 5 6',
#  '7 8 9'
# ]

# [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
