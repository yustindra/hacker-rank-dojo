#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    n_arr = len(arr)
    n_pos = 0
    n_neg = 0
    n_zero = 0
    for i in range(n_arr):
        if arr[i] > 0:
            n_pos += 1
        elif arr[i] < 0:
            n_neg += 1
        else:
            n_zero += 1
    print (round((n_pos/n_arr), 4))
    print (round((n_neg/n_arr), 4))
    print (round((n_zero/n_arr), 4))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
