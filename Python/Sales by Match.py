#The problem: https://www.hackerrank.com/challenges/sock-merchant/problem

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    top =0
    a = list(set(ar))
    
    for i in range(len(a)):
        y=ar.count(a[i])
        
        if y%2==0:
            top+=y/2
            
        if (y>1) & (y%2==1):
            top+=(y-1)/2
            
    return int(top)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
