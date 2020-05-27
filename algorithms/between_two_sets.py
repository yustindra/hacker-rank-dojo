#!/bin/python3

import math
import os
import random
import re
import sys
from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def getTotalX(a, b):
    min_gcd = reduce(gcd, b)
    max_lcm = reduce(lcm, a)
    count = 0
    for x in range(max_lcm, min_gcd+1, max_lcm):
        if min_gcd % x == 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
