#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    Alice = 0
    Bob = 0
    for i in range(0,3):
        vala = globals()["a"+str(i)]
        valb = globals()["b"+str(i)]
        if vala > valb:
            Alice+=1
        elif vala < valb:
            Bob +=1

    return Alice, Bob


if __name__ == '__main__':

    a0, a1, a2 = input().strip().split(' ')
    a0, a1, a2 = [int(a0), int(a1), int(a2)]
    b0, b1, b2 = input().strip().split(' ')
    b0, b1, b2 = [int(b0), int(b1), int(b2)]
    result = solve(a0, a1, a2, b0, b1, b2)
    print (" ".join(map(str, result)))


