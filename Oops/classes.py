class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

class Person:

    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"{self.name} is talking")

person1=Person("shivya")
person1.talk()

point1= Point(10,20)
print(point1.x)
point1.y=3
print(point1.y)
point1.move()

