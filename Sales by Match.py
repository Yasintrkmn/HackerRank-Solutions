#!/bin/python3
"""
Input olarak liste ve boyutu verildiğinde elemanlar çifter olarak eşleştirilirse kaç çift oluşur?
Örneğin, ar=[2,3,1,2,1,2,1] ve n=7 ise 2 çift oluşur.
"""
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
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
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
