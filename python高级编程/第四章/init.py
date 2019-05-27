class MyClass(object):
    def __init__(self, name):
        print("this init method:"+name)

    def __eq__(self, other):
        return type(self) == type(other)

my = MyClass("lzq")

print(MyClass("lzb") == my)

print(MyClass("123") == MyClass("456"))

print(MyClass("789") == 42)


import random

class Dice(object):
    def __init__(self, sides = 6):
        self.sides = sides

    def roll(self):
        print(random.randint(1, self.sides))

dice = Dice(20)

print(dice.sides)

dice2 = Dice()

dice.roll()

dice2.roll()