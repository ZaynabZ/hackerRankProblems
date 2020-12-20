#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#

def filledOrders(order, k):
    numberOfOrders = 0
    for o in sorted(order):
        if k >= o:
            numberOfOrders += 1
            k = k - o
    return numberOfOrders


order_count = int(input().strip())

order = []

for _ in range(order_count):
    order_item = int(input().strip())
    order.append(order_item)

k = int(input().strip())

result = filledOrders(order, k)

print(str(result))

