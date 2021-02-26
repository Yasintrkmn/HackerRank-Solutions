The problem: https://www.hackerrank.com/challenges/sherlock-and-squares/problem

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    i,c=0,0
    while True:
        if (i**2) >b:
            return c
        if ((i**2)>=a) & ((i**2) <=b):
            c+=1
        i+=1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
