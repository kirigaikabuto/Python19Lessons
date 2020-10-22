clothes = []
file = open("database.txt", 'r')
data = file.read()
# data
# футболка,20\n
# куртка,30
clothesArrStr = data.split("\n")
# clothesArrStr
# [
#     "футболка,20",
#     "куртка,30"
# ]
n = len(clothesArrStr)
i = 0
while i < n:
    print(clothesArrStr[i])
    #clothesArrStr[i] -> футболка,20
    clothesPart = clothesArrStr[i].split(",")
    clothes.append(clothesPart)
    i += 1
print(clothes)
# clothes = [
# #     ["футболка","20"],
# #     ["куртка","30"],
# # ]
# # print(clothes)
