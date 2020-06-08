#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    max_score, min_score = scores[0], scores[0]
    count_max, count_min = 0, 0
    for i in scores:
        if i < max_score:
            max_score = i
            count_max += 1
        if i > min_score:
            min_score = i
            count_min += 1
    return count_min, count_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
