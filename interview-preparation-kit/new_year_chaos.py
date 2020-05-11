#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    bribes, swaps = 0, 1
    for i, queue in enumerate(q):
        if queue > i + 3:
            print ('Too chaotic')
            return None

    while swaps != 0:
        swaps = 0
        for i in range(len(q) - 1):
            if q[i] > q[i + 1]:
                q[i], q[i + 1] = q[i + 1], q[i]
                bribes += 1
                swaps += 1
    
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        
        minimumBribes(q)
