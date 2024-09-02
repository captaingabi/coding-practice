#!/bin/python3

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Get")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Set")
        self._temperature = value


print("instantianate")
human = Celsius(37)

print("print")
print(human.temperature)

print("call to farenheit")
print(human.to_fahrenheit())

print("change value")
human.temperature = human.temperature + 1
