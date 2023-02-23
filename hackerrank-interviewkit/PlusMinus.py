"""
Hacker Rank Problem
https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    total = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for ele in arr:
        if ele > 0:
            pos += 1
        elif ele < 0:
            neg += 1
        else:
            zero += 1
    
    print("{:.6f}".format(pos/total))
    print("{:.6f}".format(neg/total))
    print("{:.6f}".format(zero/total))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
