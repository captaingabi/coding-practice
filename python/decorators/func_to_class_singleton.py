#!/bin/python3

import time


def timer(cls):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = cls(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {cls.__name__}() in {run_time:.8f} secs")
        return value
    return wrapper_timer


# This only decorates the __init__
@timer
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


person = Person("Joe")
print(person.get_name())


def singleton(cls):
    def wrapper_singleton(*args, **kwargs):
        if wrapper_singleton.instance is None:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass


first_one = TheOne()
another_one = TheOne()
print(id(first_one), id(another_one), first_one is another_one)
