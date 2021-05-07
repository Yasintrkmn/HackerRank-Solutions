# The problem: https://www.hackerrank.com/challenges/chocolate-feast/problem

import math
import os
import random
import re
import sys

def chocolateFeast(n, c, m):
    x,chc = 0, n//c
    pack = chc
    x+=chc
    
    while True:
        chc = pack//m
        pack = pack+chc-chc*m
        x+=chc
        
        if pack<m:
            return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
