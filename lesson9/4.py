clothes = [
    "футболка",
    "шуба",
    "джинсы",
]
prices = [
    250,
    1000,
    500
]
n = len(clothes)
i = 0
while i < n:
    print(f"{i}.{clothes[i]}")
    i += 1
choice = int(input("выбрать:"))
print(clothes[choice], prices[choice])
# программа спрашивает у человека что ты хочешь купить?
# 0.футболка
# 1.шуба
# 2.джинсы
# 0
# это футболка и ее цена 250
