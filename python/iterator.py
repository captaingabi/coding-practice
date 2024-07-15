#!/bin/python3

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


class MyNumbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

data = {}
keys = ["zero", "one", "two", "three", "four", "five"]
for key, value in zip(keys, myiter):
    data[key] = value

print(data)

for index, value in enumerate(keys):
    print(index, value)
