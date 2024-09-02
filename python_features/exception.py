#!/bin/python3

class OneDivisionError(Exception):
    pass


def divide(x, y):
    try:
        if y == 1:
            raise OneDivisionError("Dividing by 1 does not make sense...")
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except OneDivisionError as ex:
        print(f"{ex}")
    except Exception:
        print("Some other exception occured, re-raising")
        raise  # You cen re-raise the same exception
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 2)
print()
divide(2, 1)
print()
divide(2, 0)
print()
divide('2', '0')
print()
