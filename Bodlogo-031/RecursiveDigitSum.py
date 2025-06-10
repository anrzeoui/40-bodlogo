import math
import os
import random
import re
import sys

def superDigit(n, k):
    def recursive_sum(num_str):
        if len(num_str) == 1:
            return int(num_str)
        total = sum(int(d) for d in num_str)
        return recursive_sum(str(total))
    
    initial_sum = sum(int(d) for d in n) * k
    
    return recursive_sum(str(initial_sum))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()