import math
import os
import random
import re
import sys

def maxMin(k, arr):
    arr.sort()
    min_diff=sys.maxsize
    
    for i in range(n-k+1):
        min_diff = min(min_diff, arr[i+k-1] - arr[i])
    return min_diff
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()