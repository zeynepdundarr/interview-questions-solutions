#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    # Write your code here
    str_arr_dict = {}
    for str_a in stringList:
        if str_a not in str_arr_dict.keys():
            str_arr_dict[str_a] = 1
        else:
            str_arr_dict[str_a] += 1

    answer = ''
    for query_str in queries:
        if query_str in str_arr_dict.keys():
            answer += str(str_arr_dict[query_str]) + "\n"
        else:
            answer += '0'

    return answer

if __name__ == '__main__':
 
    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)
    print("result is: ", res)