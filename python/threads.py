#!/bin/python3

'''
Note: concuirrency vs parallelism

A global interpreter lock (GIL) is a mechanism used in
computer-language interpreters to synchronize the execution of threads
so that only one native thread (per process) can execute basic operations
(such as memory allocation and reference counting) at a time.
As a general rule, an interpreter that uses GIL will see
only one thread to execute at a time,

Note: python 3.13 will make GIL optional
'''

import threading
import os
import time


def calculate_squares(numbers):
    for num in numbers:
        square = num * num
        print(f"Square of the number {num} is {square : >3} | " +
              f"Thread Name {threading.current_thread().name} | " +
              f"PID of the process {os.getpid()}"
              )
        n = 40000000
        while n > 0:
            n = n-1


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
half = len(numbers) // 2
first_half = numbers[:half]
second_half = numbers[half:]

t1 = threading.Thread(target=calculate_squares, name="t1", args=(first_half,))
t2 = threading.Thread(target=calculate_squares, name="t2", args=(second_half,))

print(f"started at {time.strftime('%X')}")
t1.start()
t2.start()

t1.join()
t2.join()
print(f"finished at {time.strftime('%X')}")
