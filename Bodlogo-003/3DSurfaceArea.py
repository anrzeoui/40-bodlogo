import math
import os
import random
import re
import sys

def surfaceArea(A):
    H = len(A)
    W = len(A[0])
    total = 0

    for i in range(H):
        for j in range(W):
            if A[i][j] > 0:
                total += 2

                if i == 0:
                    total += A[i][j]
                else:
                    total += max(0, A[i][j] - A[i-1][j])

                # Down
                if i == H - 1:
                    total += A[i][j]
                else:
                    total += max(0, A[i][j] - A[i+1][j])

                # Left
                if j == 0:
                    total += A[i][j]
                else:
                    total += max(0, A[i][j] - A[i][j-1])

                # Right
                if j == W - 1:
                    total += A[i][j]
                else:
                    total += max(0, A[i][j] - A[i][j+1])

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()