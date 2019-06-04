print(isinstance([], list))  #输出结果True

print(isinstance(object(), list))  #输出结果Flase

print(isinstance([], (list, tuple)))  #输出结果True

print(isinstance((), (list, tuple)))  #输出结果True

print(isinstance(object(), (list, tuple)))  #输出结果Flase

print(hasattr([], '__getitem__'))  #输出结果True

print(hasattr(object(), '__getitem__'))  #输出结果Flase

print(hasattr({}, '__getitem__')) #输出结果True


import abc

class MySequence(metaclass=abc.ABCMeta):
    pass

MySequence.register(list)  #注册list

print("register list="+str(isinstance([], MySequence)))

print("register tuple="+str(isinstance((), MySequence)))

MySequence.register(tuple)   #注册tuple

print("register tuple="+str(isinstance((), MySequence)))

@MySequence.register
class CustomeListLikeClass(object):
    pass

print(issubclass(CustomeListLikeClass, MySequence))

print(isinstance(CustomeListLikeClass, MySequence))