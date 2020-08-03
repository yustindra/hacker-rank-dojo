#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(n, s):
    lvl = valley = 0
    for i in range(n):
        if s[i] == 'U':
            lvl += 1
            if lvl == 0:
                valley += 1
        else:
            lvl -= 1

    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
