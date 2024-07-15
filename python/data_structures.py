#!/bin/python3

from collections import deque
from typing import Deque

# list      ordered     mutable     duplicates
# queue     ordered     mutable     duplicates      FIFO
# stack     ordered     mutable     duplicates      LIFO
# tuple     ordered     inmutable   duplicates
# set       unordered   mutable     no duplicates
# frozenset unordered   inmutable   no duplicates
# dict      ordered     mutable     no duplicates

# list comprehension with if guard
my_list = [x*x for x in range(1, 6) if x != 3]
print(my_list)

myStack: Deque = deque()
myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
try:
    print(myStack.pop())
except IndexError:
    pass
