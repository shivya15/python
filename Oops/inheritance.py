import classes
from Basics import lists

class Dog:
    def walk(self):
        print("walk")

class Cat(Dog):

    def __init__(self) -> None:
        super().__init__()

print(lists.numbers)
cat1=Cat()
cat1.walk()
point3= classes.Point(10,20)
print(point3.x)

