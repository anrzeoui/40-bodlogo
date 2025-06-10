import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    unique_scores = sorted(set(ranked), reverse=True)
    n = len(unique_scores)
    result = []
    index = n - 1  
    for score in player:
        while index >= 0 and score >= unique_scores[index]:
            index -= 1
        result.append(index + 2)  

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()