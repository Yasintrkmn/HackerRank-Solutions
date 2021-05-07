#The problem: https://www.hackerrank.com/challenges/picking-numbers/problem

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    result=0
    
    for i in a:
        x1=a.count(i)
        x2=a.count(i-1)
        x1=x1+x2
        
        if c > result:
            result=x1
            
    return result
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
