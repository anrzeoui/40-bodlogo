import math
import os
import random
import re
import sys

def get_pluses(grid):
    rows = len(grid)
    cols = len(grid[0])
    pluses = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 'G':
                continue

            length = 0
            while True:
                try:
                    if (r - length < 0 or r + length >= rows or
                        c - length < 0 or c + length >= cols or
                        grid[r - length][c] != 'G' or
                        grid[r + length][c] != 'G' or
                        grid[r][c - length] != 'G' or
                        grid[r][c + length] != 'G'):
                        break
                except:
                    break

                cells = set()
                cells.add((r, c))  
                for i in range(1, length + 1):
                    cells.add((r - i, c))
                    cells.add((r + i, c))
                    cells.add((r, c - i))
                    cells.add((r, c + i))

                area = 1 + length * 4
                pluses.append((area, cells))
                length += 1

    return pluses


def twoPluses(grid):
    pluses = get_pluses(grid)
    max_product = 0

    for i in range(len(pluses)):
        for j in range(i + 1, len(pluses)):
            area1, cells1 = pluses[i]
            area2, cells2 = pluses[j]

            if cells1.isdisjoint(cells2):  # no overlap
                max_product = max(max_product, area1 * area2)

    return max_product


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()