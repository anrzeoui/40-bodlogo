import math
import os
import random
import re
import sys

def almostSorted(arr):
    sorted_arr = sorted(arr)
    n = len(arr)

    l, r = 0, n - 1
    while l < n and arr[l] == sorted_arr[l]:
        l += 1
    while r > l and arr[r] == sorted_arr[r]:
        r -= 1

    if l >= r:
        print("yes")
        return

    arr[l], arr[r] = arr[r], arr[l]
    if arr == sorted_arr:
        print("yes")
        print(f"swap {l+1} {r+1}")
        return

    arr[l], arr[r] = arr[r], arr[l]

    if arr[:l] + arr[l:r+1][::-1] + arr[r+1:] == sorted_arr:
        print("yes")
        print(f"reverse {l+1} {r+1}")
        return

    print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)