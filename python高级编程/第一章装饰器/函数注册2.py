class Registry(object):

    def __init__(self):
        self._function = []

    def register(self, dectory):
        self._function.append(dectory)
        return dectory

    def run_all(self, *args, **kwargs):

        return_values = []

        for func in self._function:
            return_values.append(func(*args, **kwargs))

        return return_values

a = Registry()

b = Registry()

@a.register
def foo(x=3):
    return x

@b.register
def bar(x=5):
    return x

@a.register
@b.register
def baz(x=7):
    return x

print(a.run_all())

print(b.run_all())

print(b.run_all(4))