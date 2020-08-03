#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    
    highest = max(ar)
    highest_cnt = 0
    for i in range(len(ar)):
        if ar[i] == highest:
            highest_cnt += 1
    
    return highest_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
