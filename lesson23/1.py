from cat import Cat
from dog import Dog

cat1 = Cat(name="cat1", age=10)
cat2 = Cat(name="cat2", age=12)
cat3 = Cat(name="cat3", age=1)
cat4 = Cat(name="cat4", age=13)
cats = [cat1, cat2, cat3, cat4]
maxi = cats[0].age
maxi_cat = cats[0]
for i in cats:
    if i.age > maxi:
        maxi = i.age
        maxi_cat = i

maxi_cat.printData()
