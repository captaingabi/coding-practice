#!/bin/python3

from multiprocessing import Process
import os
import time


def calculate_squares(numbers):
    for num in numbers:
        square = num * num
        print(f"Square of the number {num} is {square : >3} | " +
              f"PID of the process {os.getpid()}"
              )
        n = 50000000
        while n > 0:
            n = n-1


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
half = len(numbers) // 2
first_half = numbers[:half]
second_half = numbers[half:]

p1 = Process(target=calculate_squares, args=(first_half,))
p2 = Process(target=calculate_squares, args=(second_half,))


print(f"started at {time.strftime('%X')}")
p1.start()
p2.start()

p1.join()
p2.join()
print(f"started at {time.strftime('%X')}")
