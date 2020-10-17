s1 = "шуба футболка джинсы кофта куртка"
s2 = "210 300 500 100 1000"
clothes = s1.split(" ")
prices_str = s2.split(" ")
n = len(clothes)
prices = []
i = 0
while i < n:
    num = int(prices_str[i])
    prices.append(num)
    i += 1

i = 0
while i < n:
    print(f"{i}.{clothes[i]}")
    i += 1
choice = int(input("выбрать:"))
print(clothes[choice], prices[choice])
