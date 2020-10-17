file1 = open("clothes.txt", "r", encoding="utf-8")  # r ->read
data1 = file1.read()
clothes = data1.split("\n")
new_element = "пиджак"
clothes.append(new_element)
print(clothes)
s = "\n".join(clothes)
file2 = open("clothes.txt", "w", encoding="utf-8")
file2.write(s)
file2.close()
