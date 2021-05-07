#The problem: https://www.hackerrank.com/challenges/counting-valleys/problem

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    sum, count = 0,0
    liste=list()
    
    for i in range(steps):
        if path[i]=="D":
            liste.append(-1)
            
        else:
            liste.append(1)
            
    for k in range(steps):
        sum+=liste[k]
        
        if (sum==0) & (sum-liste[k]<0):
            count+=1
            
    return count
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
