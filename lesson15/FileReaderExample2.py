fileName = "out.txt"
file = open(fileName, "r")
data = file.readlines()
numbers = []
for i in data:
    text = i.strip("\n")
    number = int(text)
    numbers.append(number)
print(numbers)
