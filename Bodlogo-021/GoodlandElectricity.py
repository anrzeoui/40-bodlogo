import math
import os
import random
import re
import sys

def pylons(k, arr):
    n = len(arr)
    count = 0
    i = 0 
    
    while i < n:
        left = max(0, i - (k - 1))
        right = min(n - 1, i + (k - 1))
        
        plant_pos = -1
        for pos in range(right, left - 1, -1):
            if arr[pos] == 1:
                plant_pos = pos
                break
        
        if plant_pos == -1:
            return -1
        
        count += 1
        i = plant_pos + k
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()