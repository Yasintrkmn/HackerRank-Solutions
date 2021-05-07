# The problem: https://www.hackerrank.com/challenges/migratory-birds/problem

import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    s = {}
    
    for i in range(max(arr)+1):
        s[i] = arr.count(i)

    return max(s, key=s.get)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
