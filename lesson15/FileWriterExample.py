numbers = [1, 2, 3, 4, 5]
file = open("out.txt", "w")
# lines = ["1\n", "2\n", "3\n", "4\n", "5\n"]
# code join
newnumbers=[]
for i in numbers:
    newnumbers.append(str(i))
print(newnumbers)

file.writelines()
file.close()
