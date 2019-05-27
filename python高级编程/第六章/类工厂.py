class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    def go_to_dev(self):
        pass

#创建animal类方法
def create_animal_class():

    def __init__(self, name):
        self.name = name

    def eat(self):
        return 'bababa'+self.name

    def go_to_dev(self):
        pass

    #通过type方法创建类第一各参数为类名字,第二个参数为类继承的类,第三个参数为类的结构
    return type('Animal',(object,),{
        '__doc__':'test',
        '__init__': __init__,   #可以将方法名直接赋值
        'eat': eat,             #可以将方法名直接赋值
        'go_to_dev':go_to_dev   #可以将方法名直接赋值
    })

animal1 = create_animal_class()
animal2 = create_animal_class()

print(animal1.__doc__)

p = animal2('lzq').eat()

print(p)
print(isinstance(animal1, animal2))
