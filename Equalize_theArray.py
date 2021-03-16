# The problem: https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    x=0
    x = [arr.count(i) for i in range(min(arr),max(arr)+1) if arr.count(i)>x]

    return len(arr)-max(x)
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
