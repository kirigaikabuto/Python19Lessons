clothes = []
file = open("database.txt", 'r')
data = file.read()
clothesArrStr = data.split("\n")
n = len(clothesArrStr)
i = 0
while i < n:
    clothesPart = clothesArrStr[i].split(",")  # ["куртка","20"]
    clothes.append(clothesPart)
    i += 1
n = len(clothes)
i = 0
while i < n:
    print(clothes[i][0], clothes[i][1])
    i += 1

# кимано
# 30
#
# кимано, 30 -> clothes[] -> "\n" -> writeToFile
