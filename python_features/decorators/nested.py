#!/bin/python3

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=3)
@decorator
def func1(data):
    print(f"main func {data}")


func1("some data")

print()


@decorator
@repeat(num_times=3)
def func2(data):
    print(f"main func {data}")


func2("some data")
