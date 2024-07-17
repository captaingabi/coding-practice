#!/bin/python3
import weakref
import gc

from copy import copy, deepcopy


data = {"key": [1, 2]}

shallow_copy = copy(data)
deep_copy = deepcopy(data)

data["key"][0] = 111

print(f"{data=}")
print(f"{shallow_copy=}")
print(f"{deep_copy=}")


# Weak references allow you to create references to an object
# that will not increase the reference count.
class A:
    pass


obj = A()
weak_ref = weakref.ref(obj)

gc.collect()
print(f"{weak_ref() is obj=}")

obj = A()
gc.collect()
print(f"{weak_ref() is obj=}")
print(f"{weak_ref() is None=}")
