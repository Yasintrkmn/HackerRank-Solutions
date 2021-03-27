# Problem: https://www.hackerrank.com/challenges/lisa-workbook/problem

import math
import os
import random
import re
import sys

def workbook(n, k, arr):
    page=1
    f=0
    output=0
    chapter=0
    for i in arr:
        chapter+=1
        for j in range(1,i+1):
            if (f==k) | (j==i+1):
                page+=1
                f=0
            f += 1
            if page==j:
                output+=1
        page+=1
        f=0
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
