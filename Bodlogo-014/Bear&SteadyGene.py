import math
import os
import random
import re
import sys

from collections import Counter

def steadyGene(gene):
    n = len(gene)
    required = n // 4
    count = Counter(gene)

    if all(count[ch] <= required for ch in "ACGT"):
        return 0

    min_len = n
    left = 0

    for right in range(n):
        count[gene[right]] -= 1

        while all(count[ch] <= required for ch in "ACGT"):
            min_len = min(min_len, right - left + 1)
            count[gene[left]] += 1
            left += 1

    return min_len



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()