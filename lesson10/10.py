clothes = []
file = open("database.txt", 'r')
data = file.read()
clothesArrStr = data.split("\n")
#clothesArrStr->['футболка,20', 'куртка,30', 'плащ,40', 'кимано,30', 'sdsd,123']
name = input("name:")
price = input("price:")
product = name + "," + price
clothesArrStr.append(product)
s = "\n".join(clothesArrStr)
# 'футболка,20'
# 'куртка,30'
# 'плащ,40'
# 'кимано,30'
# 'sdsd,123'
newFile = open("database.txt", "w")
newFile.write(s)
newFile.close()


# n = len(clothes)
# i = 0
# while i < n:
#     print(clothes[i][0], clothes[i][1])
#     i += 1

# кимано
# 30
#
# кимано, 30 -> clothes[] -> "\n" -> writeToFile
