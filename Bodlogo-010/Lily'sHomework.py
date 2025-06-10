import math
import os
import random
import re
import sys

def min_swaps(arr, sorted_arr):
    index_map = {v: i for i, v in enumerate(arr)}
    swaps = 0
    arr = arr.copy()

    for i in range(len(arr)):
        correct_value = sorted_arr[i]
        if arr[i] != correct_value:
            to_swap_idx = index_map[correct_value]

            index_map[arr[i]] = to_swap_idx
            index_map[correct_value] = i

            arr[i], arr[to_swap_idx] = arr[to_swap_idx], arr[i]
            swaps += 1

    return swaps

def lilysHomework(arr):
    sorted_asc = sorted(arr)
    sorted_desc = sorted(arr, reverse=True)

    return min(min_swaps(arr, sorted_asc), min_swaps(arr, sorted_desc))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()