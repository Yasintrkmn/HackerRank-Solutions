#!/bin/python3
"""
Bir sporcu engebeli bir alanda yürümektedir. Yürüyüşler her zaman deniz seviyesinde başlar ve biter. D: aşağı ve U: yukarı anlamına gelir. Her bir harf bir adımı temsil eder.
Sporcunun geçtiği vadi sayısı kaçtır?
's' adımları ve 'n' adım sayısını temsil etmektedir.
input s="UDDDUDUU" ve n=8
"""
import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    sum=0
    count=0
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
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)
