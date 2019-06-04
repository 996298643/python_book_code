def requireds_int(decorated):

    def inner(*args, **kwargs):

        print(list(args))

        for key in kwargs.keys():
            print(key)

        for value in kwargs.values():
            print(value)

        kwargs_value = [i for i in kwargs.values()]

        for arg in list(args)+kwargs_value:

            if not isinstance(arg, int):
                raise TypeError("参数不能有非整型:"+decorated.__name__)

        return decorated(*args, **kwargs)

    return inner


@requireds_int
def foo(x, y):
    return x+y

print(foo(8, 9))  #可以正常运行, inner函数args有值, kwargs无值

print(foo(x=8, y=9))  #可以正常运行,　inner函数args无值, kwargs有值

#print(foo("5",9))  #抛出异常