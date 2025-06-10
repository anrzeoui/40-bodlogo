import math
import os
import random
import re
import sys

def highestValuePalindrome(s, n, k):
    s = list(s)        
    changes = [0] * n   

    l, r = 0, n - 1
    while l < r:
        if s[l] != s[r]:
            if s[l] > s[r]:
                s[r] = s[l]
            else:
                s[l] = s[r]
            changes[l] = changes[r] = 1
            k -= 1
        l += 1
        r -= 1

    if k < 0:
        return "-1" 

    l, r = 0, n - 1
    while l <= r:
        if l == r:
            if k > 0 and s[l] != '9':
                s[l] = '9'
                k -= 1
        else:
            if s[l] != '9':
                if changes[l] or changes[r]:
                    if k >= 1:
                        s[l] = s[r] = '9'
                        k -= 1
                else:
                    if k >= 2:
                        s[l] = s[r] = '9'
                        k -= 2
        l += 1
        r -= 1

    return ''.join(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()