x = int(input())
if x >= 0 and x < 10:
    print("0-10")
elif x >= 10 and x < 20:
    print("10-20")
elif x >= 20 and x < 30:
    print("20-30")
elif x >= 30 and x < 40:
    print("30-40")
else:
    print(">=40")
# x
# 10 <= x < 20 -> 10-20
# 20 <= x < 30 -> 20-30
# 30 <= x < 40 -> 30-40
# >=40
