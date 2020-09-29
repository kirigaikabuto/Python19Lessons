money = int(input("Введите выигрыш:"))
a = int(input("Процент первого:"))
b = int(input("Процент второго:"))
c = int(input("Процент третьего:"))
a_money = (a*money)/100
b_money = (b*money)/100
c_money = (c*money)/100
print(f"Первый человек выиграл {a_money}")
print(f"Второй человек выиграл {b_money}")
print(f"Третьй человек выиграл {c_money}")