#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the array2D function below.
def array2D(arr):
    a=len(arr)
    b=len(arr[0])
    max_sum=-1000
    for i in range(a-2):
        for j in range(b-2):
            sum = (arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1] + arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            
            
            if(sum>max_sum):
                max_sum=sum
    
    return max_sum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = array2D(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

