#!/bin/python3

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green, yellow, red)


def func1(a, b, c, d):
    print(a, b, c, d)


my_list = [1, 2, 3, 4]
func1(*my_list)


def mySum(*args):
    return sum(args)


print(mySum(1, 2, 3, 4, 5))


def func2(a, b, c):
    print(a, b, c)


d = {'a': 2, 'b': 4, 'c': 10}
func2(**d)


def func3(**kwargs):
    print(type(kwargs))
    print(kwargs.keys())
    print(kwargs.values())
    for key, value in kwargs.items():
        print(f"{key}, {value}")


func3(name="geeks", ID="101", language="Python")
