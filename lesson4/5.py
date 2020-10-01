a = int(input())
b = int(input())
c = int(input())
condition = input("Что нужно сделать:")
number = 0
part1 = ""
part2 = ""
if condition == "max":
    if a > b and a > c:
        number = a
    if b > a and b > c:
        number = b
    if c > a and c > b:
        number = c
    part1 = "максимальное"
elif condition == "min":
    if a < b and a < c:
        number = a
    if b < a and b < c:
        number = b
    if c < a and c < b:
        number = c
    part1 = "минимальное"
else:
    print("у нас нет такого команды")
    exit()

if number % 2 == 0:
    part2 = "четное"
else:
    part2 = "не четное"
out = f"{number} это {part1} число и оно {part2}"
print(out)
# 3
# 4
# 5
# Что нужно сделать:max
#
# Ответ: 5 это максимальное число и оно нечетное
#
# 2
# 4
# 5
# Что нужно сделать:min
#
# Ответ: 2 это минимальное число и оно четное
