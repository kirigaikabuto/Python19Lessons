balance = 200
year = 7
year_cache = 10
i = 0
while i < year:
    balance = balance + (balance*year_cache)/100
    i += 1
    print(f"year {i} and balance {balance}")
print(balance)
# 200 + 200*0.1 = 220
# 220 + 220*0.1 = 242
# 242 + 242*0.1 = 284.2
