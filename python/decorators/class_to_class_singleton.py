#!/bin/python3

class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)

        return self.instance


@Singleton
class TheOne:
    pass


first_one = TheOne()
another_one = TheOne()
print(id(first_one), id(another_one), first_one is another_one)
