#!/bin/python3

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}()")
        return self.func(*args, **kwargs)


@CountCalls
def func(data):
    print(f"main func {data}")


func("some data")
func("some data")
func("some data")
