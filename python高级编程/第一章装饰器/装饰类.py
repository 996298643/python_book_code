import functools
import time

def sortable_by_creation_time(cls):

    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self._created = time.time()

    cls.__init__=new_init

    cls.__lt__=lambda self, other: self._created < other._created

    cls.__gt__=lambda self, other: self._created > other._created

    return cls

@sortable_by_creation_time
class Sortable(object):

    def __init__(self, message):
        self._message = message

    def __repr__(self):
        return self._message

first = Sortable("first")

second = Sortable("second")

third = Sortable("third")

sortable = [second, third , first]

print(sortable)

sortable = sorted(sortable)

print(sortable)