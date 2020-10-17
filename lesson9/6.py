file = open("clothes.txt", "r")  # r ->read
data = file.read()
clothes = data.split("\n")
print(clothes)