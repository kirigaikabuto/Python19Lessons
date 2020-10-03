balance = 200
year = 7
year_cache = 10
i = 0
year_balance =0
while i < year:
    year_balance = balance + (balance*year_cache)/100
    i += 1
print(year_balance)