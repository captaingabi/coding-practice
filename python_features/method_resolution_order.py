#!/bin/python3

# Uses C3 Linearization Algorithm

class A:
    @classmethod
    def func(cls):
        print(f"In class {cls.__name__}")


class B:
    @classmethod
    def func(cls):
        print(f"In class {cls.__name__}")


class C(A, B):
    pass


class D(B, A):
    pass


A.func()
B.func()
C.func()
D.func()
print(C.__mro__)
print(D.__mro__)

# Both mypy and runtime excpetion errors about the impossible mro
# class E(C, D):
#     pass
