#!/bin/python3

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=3)
def func(data):
    print(f"main func {data}")


func("some data")
