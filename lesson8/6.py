# вводятся n чисел и среди них нужно найти
# максимальное
# минимальное
# и среднее арифмитическое
#
# 3
# 4
# 5
# 6
# Максимальное число:6
# Минимальное число:4
# Среднее ариф:5
n = int(input())
i = 0
arr = []
while i < n:
    num = int(input())
    arr.append(num)
    i += 1

maxi = arr[0]
i = 0
while i < n:
    if arr[i] > maxi:
        maxi = arr[i]
    i += 1
print(f"максимальное число {maxi}")

mini = arr[0]
i = 0
while i < n:
    if arr[i] < mini:
        mini = arr[i]
    i += 1
print(f"минимальное число:{mini}")

sumi = 0
i = 0
while i < n:
    sumi = sumi + arr[i]
    i+=1

print(f"среднее ариф:{sumi/n}")