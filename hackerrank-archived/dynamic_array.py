#!/bin/python3

import math
import os
import random
import re
import sys


def dynamicArray(n, queries):

    lastAnswer = 0
    seqList = []
    for i in range(n):
        seqList.append([])
    output = []
    for o, x, y in queries:
        index = (x ^ lastAnswer) % n
        if o == 1:
            seqList[index].append(y)
        if o == 2:
            size = len(seqList[index])
            lastAnswer = seqList[index][y % size]
            output.append(lastAnswer)

    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
