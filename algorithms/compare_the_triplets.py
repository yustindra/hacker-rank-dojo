#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    al = 0
    bb = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            al += 1
        if a[i] < b[i]:
            bb += 1
    return [al, bb]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
