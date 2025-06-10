import math
import os
import random
import re
import sys

def biggerIsGreater(w):
    char_list = list(w)
    n = len(char_list)

    for i in range(n - 1, 0, -1):
        if char_list[i] > char_list[i - 1]:
            break
    else:
        return 'no answer'

    first_small = i - 1
    next_large = i

    for j in range(i + 1, n):
        if char_list[j] > char_list[first_small] and char_list[j] < char_list[next_large]:
            next_large = j

    char_list[first_small], char_list[next_large] = char_list[next_large], char_list[first_small]

    char_list[i:] = sorted(char_list[i:])

    return ''.join(char_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for _ in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
