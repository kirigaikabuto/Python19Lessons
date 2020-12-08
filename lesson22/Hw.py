class Group:
    def __init__(self, name):
        self.name = name


class Person:
    def __init__(self, firstName, lastName, group):
        self.name = firstName + " " + lastName
        self.group = group

    def printData(self):
        print(self.name, self.group.name)


g1 = Group(name="group1")
p1 = Person("yerassyl", "tleugazy", g1)
p1.printData()
