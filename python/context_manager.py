#!/bin/python3

class HelloContextManager:

    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        print(f" exc_type:  {exc_type}")
        print(f" exc_value: {exc_value}")
        print(f" exc_tb:    {exc_tb}")


with HelloContextManager() as hello:
    print(hello)

with HelloContextManager() as hello:
    print(hello)
    hello[100]
