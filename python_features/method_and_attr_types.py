#!/bin/python3

from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def instance_method(self):
        pass

    @staticmethod  # optional, not enforced
    @abstractmethod
    def static_method():
        pass

    @classmethod  # optional, not enforced
    @abstractmethod
    def class_method(cls):
        pass


class Derived(Base):
    class_attr = "Some Class Attribute"

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    # instance method
    def instance_method(self):
        print("Instance methods get self and called on object.")
        print(f"{self.class_attr}")
        print(f"{self.instance_attr}")
        print()

    @staticmethod
    def static_method():
        print("Static methods does not get anything (self|cls)" +
              "and called on class or on object")
        print()

    @classmethod
    def class_method(cls):
        print("Class methods get cls and called on class or on object.")
        print(f"{cls.__name__}")
        print(f"{cls.class_attr}")
        print()


obj = Derived("Some Instance Attribute")
obj2 = Derived("Some Instance Attribute 2")

obj.instance_method()
obj2.instance_method()
# Derived.instance_method()  # Classes cannot call instance methods

obj.static_method()
obj2.static_method()
Derived.static_method()

obj.class_method()
obj2.class_method()
Derived.class_method()

print()
print(f"{obj.class_attr=}")
print(f"{obj.instance_attr=}")

print()
print(f"{obj2.class_attr=}")
print(f"{obj2.instance_attr=}")

print()
print(f"{Derived.class_attr=}")
# print(f"{Derived.instance_attr=}")  # 'Derived' has no 'instance_attr'
