import math
import os
import random
import re
import sys

def powerSum(X, N, num=1):
    power = num ** N
    if power > X:
        return 0
    if power == X:
        return 1

    # Count including num and excluding num
    return powerSum(X - power, N, num + 1) + powerSum(X, N, num + 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()