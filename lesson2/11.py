a = input("Введите сумму займа:")
b = input("Введите процент:")
money = int(a)
percent = int(b)
percent_money = (money * percent) / 100
total = money + percent_money
s = f"Вы должны оплатить {total} при том что {money} долг  а {percent_money} вышла как процент"
print(s)
#Вы должны оплатить 275 при том что 250 долг  а 25 вышла как процент
