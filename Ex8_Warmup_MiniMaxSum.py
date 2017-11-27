#!/bin/python3

import sys
if __name__ == '__main__':
    arr = list(map(int, input().strip().split(' ')))
    nmbrs = len(arr)
    arr.sort()
    print (sum(arr[:nmbrs-1]), sum(arr[1:]))