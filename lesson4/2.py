# 2)
# вводятся три числа из клавиатуры a,b,c это стороны треугольника, если треугольник может существвоать то напишите YES иначе NO
# ВВОД:
# a=3
# b=4
# c=5
#
# ВЫВОД:
# YES
#
# ТЕОРИЯ: найти условия при котором треугольник может существовать

a = int(input())
b = int(input())
c = int(input())

if a+b > c and a+c > b and c+b > a:
    print("YES")
else:
    print("NO")
