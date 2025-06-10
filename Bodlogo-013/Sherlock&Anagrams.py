import math
import os
import random
import re
import sys

def sherlockAndAnagrams(s):
    substrings = {}
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            key = ''.join(sorted(sub))
            if key in substrings:
                substrings[key] += 1
            else:
                substrings[key] = 1
    count = 0
    for key in substrings:
        freq = substrings[key]
        count += freq * (freq - 1) // 2

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()