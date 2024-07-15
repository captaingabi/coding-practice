#!/bin/python3

glob = "global"


def myfunc():
    glob = "global overwritten"
    local = "local"
    global local_global
    local_global = "local declared as global"
    print("inside")
    print(glob)
    print(local_global)
    print(local)
    print()

    def myinnerfunc():
        print("inside inside")
        print(glob)
        print(local_global)
        print(local)
        print()

    myinnerfunc()


myfunc()

print("outside")

print(glob)
# print(local_global)  # mypy errors, but works, still shall mever do this
# print(local)  # even flake8 errors
