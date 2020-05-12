#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    cnt_apples, cnt_oranges = 0, 0
    for x in apples:
        if s <= x + a <= t:
            cnt_apples += 1
    for y in oranges:
        if s <= y + b <= t:
            cnt_oranges += 1
    
    print (cnt_apples)
    print (cnt_oranges)
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
