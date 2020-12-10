class Rectangle:
    def __init__(self, a, b):
        self.width = a
        self.height = b

    def printData(self):
        out = f"Rectangle->({self.width},{self.height})"
        print(out)

    def getArea(self):
        s = self.width * self.height
        return s
