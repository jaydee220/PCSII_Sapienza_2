#!/bin/python3

import sys

if __name__ == '__main__':

    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    positive = 0
    negative = 0
    zero = 0
    for val in arr:
        if val < 0:
            negative += 1
        elif val > 0:
            positive +=1
        else:
            zero += 1

    print (positive/n)
    print (negative/n)
    print (zero/n)

