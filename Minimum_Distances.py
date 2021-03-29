# Problem: https://www.hackerrank.com/challenges/minimum-distances/problem

import math
import os
import random
import re
import sys

def minimumDistances(a):
    liste=[]
    for x in range(min(a),max(a)+1):
        d = [i for i, n in enumerate(a) if n == x]
        if len(d)>1:
            liste.append(abs(d[0]-d[1]))
    if len(liste)==0:
        return -1
    return min(liste)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
