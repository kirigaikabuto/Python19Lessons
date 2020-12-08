# класс
class PersonClass:
    name = ""
    age = 0

    # конструктор initialization
    def __init__(self, externalName, externalAge):
        self.name = externalName
        self.age = externalAge

    def printData(self):
        print(self.name, self.age)
