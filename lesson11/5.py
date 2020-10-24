n = int(input())
arr = []
for i in range(n):
    s = input()  # yerassyl,22
    name, age = s.split(",")  # ["yerassyl","22"]
    age = int(age)
    arr.append([name, age])
maxi = 0
current = []
# while -> i -> index of element of array
#for i in range(n) -> index of element of array
# for i-> element of array
for i in arr:
    # i->['zhina', 23]
    # i[0]->zhina
    # i[1]->23
    if maxi < i[1]:
        maxi = i[1]
        current = i
print(current)
# 3
# yerassyl,22
# anel,21
# zhina,23
# Otvet:yerassyl 22
