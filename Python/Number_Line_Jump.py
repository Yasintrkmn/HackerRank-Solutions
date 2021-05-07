#The problem: https://www.hackerrank.com/challenges/kangaroo/problem#:~:text=You%20are%20choreographing%20a%20circus,rate%20of%20meters%20per%20jump.

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if v1==v2:
        return "NO"
      
    t = (x1 - x2) / (v2 - v1)
    
    if (t>0) & (t==int(t)):
        return "YES"
    
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
