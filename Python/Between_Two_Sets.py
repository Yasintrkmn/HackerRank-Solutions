# The problem: https://www.hackerrank.com/challenges/between-two-sets/problem

import math
import os
import random
import re
import sys
from math import gcd

def getTotalX(a, b):
    count, liste, liste2, lcm = 0, [], [], a[0]

    for i in a[1:]:
        lcm = lcm * i // gcd(lcm, i)

    for i in range(lcm,min(b)+1,lcm):
        liste.append(i)

    for j in liste:
        count=0
        
        for k in b:
            if k%j !=0:
                count=1
                continue
                
        if count==0:
            liste2.append(j)

    return len(liste2)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
