registry = []

def register(decotory):
    registry.append(decotory)
    return decotory

@register
def bar():
    return 3

@register
def foo():
    return 5

for func in registry:
    print(func())

