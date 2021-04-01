# The problem: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

import math
import os
import random
import re
import sys

def hackerrankInString(s):
    s2 = "hackerrank"
    i = 0

    for x in s:
        if x== s2[i]:
            i+=1
        if i==len(s2):
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
