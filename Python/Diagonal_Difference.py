# The problem: https://www.hackerrank.com/challenges/diagonal-difference/problem

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    lt,tl=0,0
    j=len(arr)-1
    
    for i in range(len(arr)):
        lt += arr[i][i]
        tl += arr[i][j]
        j-=1
        
    return abs(tl-lt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
