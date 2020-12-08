# width,height,address
class Home:
    def __init__(self, exWidth, exHeight, exAddress):
        self.width = exWidth
        self.height = exHeight
        self.address = exAddress

    def printData(self):
        output = f"Home with width {self.width} and height {self.height} is placed by address {self.address}"
        print(output)

    def printArea(self):
        area = self.width * self.height
        print(area)


h1 = Home(exWidth=10, exHeight=20, exAddress="egizbaeva7/9")
h1.printData()
h1.printArea()

h2 = Home(exWidth=20, exHeight=30, exAddress="sdsdsdsds")
h2.printData()
h2.printArea()
