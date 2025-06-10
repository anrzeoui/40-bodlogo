import math
import os
import random
import re
import sys

def shortPalindrome(s):
    MOD = 10**9 + 7
    
    count1 = [0]*26
    count2 = [[0]*26 for _ in range(26)]
    count3 = [[0]*26 for _ in range(26)]
    
    result = 0
    
    for ch in s:
        c = ord(ch) - ord('a')
        
        for b in range(26):
            result += count3[c][b]
        
        
        for a in range(26):
            count3[a][c] += count2[a][c]
            count3[a][c] %= MOD
        
        for a in range(26):
            count2[a][c] += count1[a]
            count2[a][c] %= MOD
        count1[c] += 1
        count1[c] %= MOD
    
    return result % MOD



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()