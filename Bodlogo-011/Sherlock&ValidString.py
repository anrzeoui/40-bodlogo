import math
import os
import random
import re
import sys

def isValid(s):
    from collections import Counter

    freq = Counter(s)

    freq_values = list(freq.values())
    freq_count = Counter(freq_values)

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) == 2:
        keys = list(freq_count.keys())
        val1, val2 = keys[0], keys[1]
        count1, count2 = freq_count[val1], freq_count[val2]

        
        if (val1 == 1 and count1 == 1) or (val2 == 1 and count2 == 1):
            return "YES"

        if (abs(val1 - val2) == 1) and (count1 == 1 or count2 == 1):
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()