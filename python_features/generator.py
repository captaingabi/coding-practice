#!/bin/python3

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sum(firstn(1000000)))


def generator():
    yield "one"
    yield "two"
    yield "three"


for item in generator():
    print(item)

gen_obj = generator()

try:
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
except StopIteration as ex:
    print("Exception occured")
    print(type(ex))
    print(ex.args)
    print(ex)
