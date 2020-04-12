#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arr_sum = sum(arr)
    arr_min = min(arr)
    arr_max = max(arr)

    min_sum, max_sum = arr_sum - arr_max, arr_sum - arr_min

    print (min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
