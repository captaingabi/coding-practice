#!/bin/python3

class LoggedAccess:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        print(f"__get__: {self.public_name} => {value}")
        return value

    def __set__(self, obj, value):
        print(f"__set__: {self.public_name} => {value}")
        setattr(obj, self.private_name, value)


class Person:

    name = LoggedAccess()                # First descriptor instance
    age = LoggedAccess()                 # Second descriptor instance

    def __init__(self, name, age):
        self.name = name                 # Calls the first descriptor
        self.age = age                   # Calls the second descriptor

    def birthday(self):
        self.age += 1


print("instantianate")
peter = Person('Peter P', 10)
print(f"{vars(peter)=}")
print("birthday")
peter.birthday()
