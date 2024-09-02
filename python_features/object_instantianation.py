#!/bin/python3

class Person:
    # use cases to override __new__:
    # Singleton pattern
    # Metaclasses
    # class UppercaseTouple(touple)
    # EncryptedFile("...") returnin different encryption classes
    def __new__(cls, name, age):
        print("__new__")
        instance = super().__new__(cls)
        return instance  # important! reutrn an instance!

    def __init__(self, name, age):
        print("__init__")
        self.name = name
        self.age = age

    def __enter__(self):
        print("__enter__")
        return self  # improtant!

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("__exit__")

    def __del__(self):
        print("__del__")

    def __str__(self):
        return (f"Person's name: {self.name}, age: {self.age}")

    def __repr__(self):
        return (f"Person('{self.name}', {self.age})")


with Person('John Doe', 30) as person:
    print(person)
    print(repr(person))
