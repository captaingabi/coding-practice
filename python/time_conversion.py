#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
"""
def timeConversion(s):
    if s[-2:] == "AM" and s[0:2] == "12":
        return "00" + s[2:-2]
    if s[-2:] == "PM" and s[0:2] != "12":
        return str(int(s[0:2]) + 12) + s[2:-2]
    
    return s[:-2]
"""

def timeConversion(s):
    return datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    print(result)

    fptr.close()
