#!/bin/python3

from functools import reduce


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

print(list(map(lambda item: item.upper(), ['cat', 'dog', 'cow'])))
print(list(filter(lambda item: 'o' in item, ['cat', 'dog', 'cow'])))
print(reduce(lambda acc, item: f'{acc}{item}', ['cat', 'dog', 'cow']))

ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids))  # Lexicographic sort
print(sorted(ids, key=lambda x: int(x[2:])))  # Integer sort
