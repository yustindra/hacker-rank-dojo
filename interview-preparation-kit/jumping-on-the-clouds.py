#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):

    jump = 0
    idx = 0

    while idx < len(c):
        if idx + 2 < len(c) and c[idx + 2] == 0:
            jump += 1
            idx += 2
        elif idx + 1 < len(c) and c[idx + 1] == 0:
            jump += 1
            idx += 1
        else:
            idx += 1

    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
