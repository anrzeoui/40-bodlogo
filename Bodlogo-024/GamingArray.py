import math
import os
import random
import re
import sys

def gamingArray(arr):
    max_so_far = 0
    count = 0
    for num in arr:
        if num > max_so_far:
            max_so_far = num
            count += 1
    return "BOB" if count % 2 else "ANDY"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()