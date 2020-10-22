clothes = []
file = open("database.txt", 'r')
data = file.read()
clothesArrStr = data.split("\n")
name = input("name:")
price = input("price:")
product = name + "," + price
clothesArrStr.append(product)
s = "\n".join(clothesArrStr)
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
