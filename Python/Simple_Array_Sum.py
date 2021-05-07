#The problem: https://www.hackerrank.com/challenges/simple-array-sum/problem

import os
import sys

def simpleArraySum(ar):
    return sum(ar)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    print(ar)
    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
