n = int(input())
arr = []
for i in range(n):
    s = input()  # yerassyl,22
    name, age = s.split(",")  # ["yerassyl","22"]
    age = int(age)
    arr.append([name, age])
maxiLen = 0
current = []
for i in arr:
    if maxiLen < len(i[0]):
        current = i
        maxiLen = len(i[0])
print(current)
# #arr->[
#     ["yerassyl",20]
#     ...
# ]
# #3
# #yerasyl,20
# #kirito,30
# #lala,40
# yerassyl,20