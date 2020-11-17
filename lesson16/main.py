a = ["yerassyl", 16, 2000, 2]
b = ["kirito", 18, 3000, 3]
c = ["lasdlsd", 22, 400, 4]
peoples = [a, b, c]
for person in peoples:
    print(person[0], person[1], person[2])

sumi = 0
for person in peoples:
    sumi += person[2]
n = len(peoples)
print(sumi / n)
