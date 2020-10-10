# Вычислить факториал введенного числа.
# Факториалом числа называют произведение всех натуральных чисел до этого числа включительно. Например, факториал числа 4 равен 1*2*3*4 = 24. Записывается факториал так: 4! = 24.
# Поскольку факториал резко увеличивается с каждым следующим числом не следует вводить больших чисел.
# Присвоим переменной, накапливающей произведение натуральных чисел, начальное значение 1.
# Присвоим переменной-счетчику значение 2.
# Пока переменная счетчик не достигнет числа, введенного пользователем,
# умножать значение переменной, в которой накапливается произведение, на значение переменной счетчика,
# увеличивать счетчик на 1
n = int(input())
f = 0
if n > 0: f = 1
for i in range(2,n+1):
    f *= i
print(f)