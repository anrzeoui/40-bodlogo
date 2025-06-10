import math
import os
import random
import re
import sys

def minimumLoss(prices):
    price_year = [(price, i) for i, price in enumerate(prices)]
    
    price_year.sort(reverse=True)

    min_loss = float('inf')

    for i in range(len(price_year) - 1):
        buy_price, buy_year = price_year[i]
        sell_price, sell_year = price_year[i + 1]

        if sell_year > buy_year:
            loss = buy_price - sell_price
            if loss < min_loss:
                min_loss = loss

    return min_loss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()