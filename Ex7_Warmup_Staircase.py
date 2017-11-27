#!/bin/python3

import sys

if __name__ == '__main__':


    n = int(input().strip())
    indent = "{:>"+str(n)+"}"
    for i in range(1,n+1):
        val = "#"*(i)
        print (indent.format(val))