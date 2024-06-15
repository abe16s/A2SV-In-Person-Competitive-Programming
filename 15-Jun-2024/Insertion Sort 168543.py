# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1,n):
        ke=arr[i]
        j=i-1
        while j>=0 and ke<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            for l in arr:
                print(l,end=" ")
            print()
        arr[j+1]=ke
    for l in arr:
        print(l,end=" ")    
    
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
