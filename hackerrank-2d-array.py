#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#



def find_hourglass_pattern(i,j, arr):
    sum_a= sum(arr[i][j:j+3]) + sum(arr[i+2][j:j+3]) + arr[i+1][j+1]
    return sum_a


def hourglassSum(arr):
    # Write your code here
    max=-63
    for i in range(0, len(arr)-2):
        for j in range(0, len(arr)-2):
            temp_max = find_hourglass_pattern(i,j, arr)
            if temp_max > max:
                max = temp_max
    return max

arr = 
[[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))

