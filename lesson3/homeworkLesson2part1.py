# 1) посчитать долю каждого человека
# 3 Человека выиграли большой куш (money) в казино и теперь хотят разделить
# их на проценты -> a,b,c и нужно определить сколько получит каждый
# из участников
money = input("Введите выигрыш:")
money_int = int(money)
first = input("Процент первого:")
a = int(first)
second = input("Процент второго:")
b = int(second)
third = input("Процент третьего:")
c = int(third)
a_money = (a*money_int)/100
b_money = (b*money_int)/100
c_money = (c*money_int)/100
a_out = f"Первый человек выиграл {a_money}"
b_out = f"Второй человек выиграл {b_money}"
c_out = f"Третьй человек выиграл {c_money}"
print(a_out)
print(b_out)
print(c_out)