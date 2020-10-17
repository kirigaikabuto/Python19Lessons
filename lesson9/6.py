# clothes
file1 = open("clothes.txt", "r")  # r ->read
data1 = file1.read()
clothes = data1.split("\n")
n = len(clothes)
# prices
file2 = open("prices.txt", "r")
data2 = file2.read()
prices_str = data2.split("\n")
i = 0
prices = []
while i < n:
    num = int(prices_str[i])
    prices.append(num)
    i += 1
#main
i = 0
while i < n:
    print(f"{i}.{clothes[i]}")
    i += 1
choice = int(input("выбрать:"))
print(clothes[choice], prices[choice])