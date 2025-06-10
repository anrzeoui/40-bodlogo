import math
import os
import random
import re
import sys

def getMinimumCost(k, c):
    m = 1
    n = len(c)
    result = 0
    c.sort(reverse=True)
    for i in range(n):
        result+=c[i]*m
        if (i+1) % k==0:
            m=m+1
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()