import math
import os
import random
import re
import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    obstacle_set = set((r, c) for r, c in obstacles)

    directions = [
        (1, 0),   
        (-1, 0),  
        (0, 1),   
        (0, -1), 
        (1, 1),  
        (1, -1),  
        (-1, 1),  
        (-1, -1) 
    ]

    count = 0
    for dr, dc in directions:
        r, c = r_q, c_q
        while True:
            r += dr
            c += dc

            if r < 1 or r > n or c < 1 or c > n:
                break
            if (r, c) in obstacle_set:
                break
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()