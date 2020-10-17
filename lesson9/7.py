# 1.посмотреть каталог
# 2.добавить новый товар
# 3.удалить товар
# 4.выйти из программы
# инициализация данных
# clothes
file1 = open("clothes.txt", "r", encoding="utf-8")  # r ->read
data1 = file1.read()
clothes = data1.split("\n")
n = len(clothes)
# prices
file2 = open("prices.txt", "r")
data2 = file2.read()
prices_str = data2.split("\n")
i = 0
prices = []
while i < n:
    num = int(prices_str[i])
    prices.append(num)
    i += 1
#меню
print("1.посмотреть каталог")
print("2.добавить новый товар")
print("3.удалить товар")
print("4.выйти из программы")
k = int(input())
if k == 1:
    print("это каталог")
    i = 0
    while i < n:
        print(f"{i}.{clothes[i]}")
        i += 1
    choice = int(input("выбрать:"))
    print(clothes[choice], prices[choice])

elif k == 2:
    print("добавить новый товар")
    name = input("введите название нового товара:")
    clothes.append(name)
    s = "\n".join(clothes)
    file3 = open("clothes.txt", "w")
    file3.write(s)
    file3.close()

elif k == 3:
    print("удалить товар")
elif k == 4:
    print("выйти из программы")
else:
    print("ошибка")