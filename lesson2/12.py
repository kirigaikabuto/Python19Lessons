#(a+b)*(c+d)
# Введите значение для a:3
# # Введите значение для b:4
# # Введите значение для с:5
# # Введите значение для d:6
# #
# # Ответ на решение был:77

a = input("Введите значение для a:")
b = input("Введите значение для b:")
c = input("Введите значение для с:")
d = input("Введите значение для d:")
number1 = int(a)
number2 = int(b)
number3 = int(c)
number4 = int(d)
part1 = number1+number2
part2 = number3+number4
part3 = part1 * part2
s = f"Ответ на решение был:{part3}"
print(s)
