# !=,==,>,<,<=,>=
# c = 10 % 3
# # 13 % 3 = 1
# # 13 - 12 = 1
a = int(input("введите первое число"))
b = int(input("введите второе число"))
#a/b без остатка
if a%b == 0:
    print("YES")
else:
    print("NO")