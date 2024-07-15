#!/bin/python3

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@decorator  # equivalent to "func = decorator(func)"
def func():
    print("main func")


func()


def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper


@decorator2
def func2(data):
    print(f"main func2 {data}")


func2("some data")
