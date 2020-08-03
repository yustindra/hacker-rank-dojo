#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    result = 0
    for n in range(m):
        for i in range(n, len(s), m):
            if sum(s[i:i+m]) == d:
                result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
