#The problem: https://www.hackerrank.com/challenges/the-hurdle-race/problem

import math
import os
import random
import re
import sys

def hurdleRace(k, height):
    if k < max(height):
        return max(height) - k
      
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
