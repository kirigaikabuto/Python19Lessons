money = 250
percent = 5
money_limit = 400
i = 0
while money < money_limit:
    money = money + (money*percent)/100
    if money >= money_limit:
        break
    i += 1
print(i)