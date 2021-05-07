#The problem: https://www.hackerrank.com/challenges/grading/problem

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.

def gradingStudents(grades):
    liste=[]
    for i in range(len(grades)):
        x = math.ceil(grades[i]/5)*5

        if (grades[i]<38) or (x-grades[i]>2):
            liste.append(grades[i])

        else:
            liste.append(x)
            
    return liste
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
