#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(height, width):
    MOD = (10**9 + 7)
    width_combinations = [1,1,2,4,8]

    while len(width_combinations) <= width:
        width_combinations.append(sum(width_combinations[-4:]) % MOD)

    total = [pow(item, height, MOD) for item in width_combinations]

    unstable = [0, 0]

    for i in range(2, width + 1):
        function = lambda j: (total[j] - unstable[j]) * total[i - j]
        result = sum(map(function, range(1, i)))
        unstable.append(result % MOD)

    return (total[m] - unstable[m]) % MOD


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
