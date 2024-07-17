#!/bin/python3
import timeit

# from memoization import cached  # Pre 3.2
from functools import lru_cache  # from 3.2, better
from statistics import mean


# DP = Recustion + Memoization

# Normal recursion:
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# print(fib(50)) #  Very slow!


# Recusrion with cache:
@lru_cache
def fib_memo(n):
    if n <= 2:
        return 1
    else:
        return fib_memo(n-1) + fib_memo(n-2)


print(mean(timeit.repeat(lambda: fib_memo(50), number=100000)))


# Recusrion with own memo variable
memo: dict = {}


def fib_memo_own(n):
    if n in memo:
        return memo[n]

    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fib_memo_own(n-1) + fib_memo_own(n-2)

    return memo[n]


print(mean(timeit.repeat(lambda: fib_memo_own(50), number=100000)))


# Bottom-Up approach:
def fib_bottom_up(n):
    memo = {}
    for i in range(1, n + 1):
        if i <= 2:
            memo[i] = 1
        else:
            memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


print(mean(timeit.repeat(lambda: fib_bottom_up(50), number=100000)))
