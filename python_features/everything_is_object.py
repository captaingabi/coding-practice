#!/bin/python3

def func():
    pass


class MyClass:
    attr = 0

    def __init__(self):
        pass

    def func(self):
        pass


for item in None, False, str, dict, func, MyClass:
    print(dir(item))
    print()
