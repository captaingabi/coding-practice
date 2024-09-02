#!/bin/python3
# import pdb ; pdb.set_trace()
# Can also be run: python3 -m pdb <*.py>

def double(x):
    breakpoint()
    return x * 2


val = 3
print(f"{val} * 2 is {double(val)}")
