arr = []
s = ""
while s != "!":
    s = input()
    arr.append(s)
arr.remove('!')
numbers = []
for i in arr:
    numbers.append(int(i))
print(numbers)
# 3
# 4
# 5
# 3
# 1
# 23
# !
