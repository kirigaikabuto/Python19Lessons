# создается изначальо массив который состоит из цифр
# от 1 до 10 и найти сумму всех элементов
# [1,2,3...]
# arr =[]
# ...
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
i = 0
sumi = 0
while i < n:
    sumi = sumi + arr[i]
    i += 1
print(sumi)