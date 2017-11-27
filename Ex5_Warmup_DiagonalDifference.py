#!/bin/python3

import sys

if __name__ == '__main__':

    n = int(input().strip())
    a = []
    sum1 = 0
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        sum1 = sum1 + (a_t[a_i] - a_t[n-1-a_i])

    if sum1 < 0:
        print (sum1*(-1))
    else:
        print (sum1)
