#!/bin/python3

# NOTE: - good when you know all the atributes and
#         functions of a class before runtime.
#       - once slots used, you cannot add dynamically
#         more attributes/functions to the object

import timeit

from dataclasses import dataclass
from statistics import mean


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class PersonSlots:
    __slots__ = "name", "age"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


@dataclass(slots=False)
class PersonDataClass:
    name: str
    age: int


@dataclass(slots=True)
class PersonDataClassSlots:
    name: str
    age: int


def test(
    person: Person | PersonSlots | PersonDataClass | PersonDataClassSlots
):
    person.age = 43
    _ = person.age
    del person.age


# Normal classes
person = Person("John", 42)
person_slots = PersonSlots("John", 42)
no_slots = mean(timeit.repeat(lambda: test(person), number=1000000))
slots = mean(timeit.repeat(lambda: test(person_slots), number=1000000))
print(f"No slots: {no_slots}")
print(f"Slots: {slots}")
print(f"% performance improvement: {(no_slots - slots) / no_slots:.2%}")

# Data classes
person_data = PersonDataClass("John", 42)
person_data_slots = PersonDataClassSlots("John", 42)
no_slots = mean(timeit.repeat(lambda: test(person_data), number=1000000))
slots = mean(timeit.repeat(lambda: test(person_data_slots), number=1000000))
print(f"Dataclass No slots: {no_slots}")
print(f"Dataclass Slots: {slots}")
print(f"% performance improvement: {(no_slots - slots) / no_slots:.2%}")
