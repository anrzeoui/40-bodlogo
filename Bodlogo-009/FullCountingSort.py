import math
import os
import random
import re
import sys

def countSort(arr):
    # Write your code here
    result = [[] for i in range(100)]
    
    for i in range(n//2):
        result[int(arr[i][0])].append('-')
    for i in range(n//2,n):
        result[int(arr[i][0])].append(arr[i][1])
    for string in result:
        if string:
            print(*string,end=' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)