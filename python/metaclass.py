#!/bin/python3

from types import NoneType


class Foo:
    pass


for t in bool, \
         str, \
         int, float, complex, \
         list, tuple, range, \
         dict, \
         set, frozenset, \
         bytes, bytearray, memoryview, \
         NoneType, \
         type, \
         Foo:
    print(type(t))


# Runtime class creation
'''
class Bar(Foo):
    attr = 100
'''
Bar = type('Bar', (Foo,), dict(attr=100))


'''
class Bar(Foo):
    def __init__(self, attr):
        self.attr = attr
'''


def init_func(self, attr):
    self.attr = attr


Bar = type('Bar', (Foo,), dict(__init__=init_func))

obj = Bar(100)
print(type(obj), obj, obj.attr)


# Custom metaclass, redefine __new__. Note: type.__new__ cannot be redefined
# NOTE: same can be achieved with Simple Inheritance or Class Decorators

class MyMetaClass(type):
    attr: int  # Needed for mypy

    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        new_cls.attr = 100
        return new_cls


class MyClass(metaclass=MyMetaClass):
    pass


print(MyClass.attr)
