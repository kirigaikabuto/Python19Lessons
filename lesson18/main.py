s = input("write something:")
l = input("write something:")
number1 = 0
number2 = 0
if s.isnumeric():
    number1 = int(s)
else:
    print("Need Only numbers")
    exit()

if l.isnumeric():
    number2 = int(l)
else:
    print("Need Only numbers")
    exit()

print(number1 + number2)
