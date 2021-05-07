#The problem: https://www.hackerrank.com/challenges/plus-minus/problem

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p,n,z=0,0,0
    for i in arr:
        p += (i>0)
        n += (i<0)
        z += (i==0)
        
    print(p / len(arr), n / len(arr), z / len(arr),sep="\n")
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
