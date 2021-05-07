#The problem: https://github.com/Yasintrkmn/HackerRank-Solutions/blob/main/Repeated%20String

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    length = s.count('a')
    s1=""
    g = int(n / len(s))
    length1 = length * g

    for i in range(n%len(s)):
        s1+=s[i]

    return length1+s1.count('a')

if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)
