a = input("Введите сумму займа:")
b = input("Введите процент:")
money = int(a)
percent = int(b)/100
total = money+(money*percent)
print(total)