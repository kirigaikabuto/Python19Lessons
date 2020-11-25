def toInt(s):
    number = 0
    if s.isnumeric():
        number = int(s)
    else:
        print("Need Only numbers")
        exit()
    return number


a = input("a=")
b = input("b=")
a = toInt(a)
b = toInt(b)
p = 2 * (a + b)
print(f"Периметр={p}")
