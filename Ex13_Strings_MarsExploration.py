#!/bin/python3

import sys

if __name__ == '__main__':
    S = input().strip()
    count = 0
    l = [S[i:i + 3] for i in range(0, len(S), 3)]
    for msg in l:
        if "S" not in msg[0]:
            count += 1
        if "O" not in msg[1]:
            count += 1
        if "S" not in msg[2]:
            count += 1
    print (count)