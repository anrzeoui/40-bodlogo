import math
import os
import random
import re
import sys

def theGreatXor(x):
    m = 1
    while m <= x:
        m <<= 1
    return m - x - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        x = int(input().strip())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()