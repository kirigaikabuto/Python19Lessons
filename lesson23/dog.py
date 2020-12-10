class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printData(self):
        output = "Dog Name:{} and  Age:{}".format(self.name, self.age)
        print(output)
