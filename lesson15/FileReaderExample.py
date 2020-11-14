fileName = "info.txt"
file = open(fileName, "r")
# data = file.readline()#read only first row
# dataLines = file.readlines()#read all lines and each line add to array
# print(dataLines[0])
data = file.read()
print(data[0])

# print("Hello my \n name is Yerassyl")
