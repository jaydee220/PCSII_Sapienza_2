#!/bin/python3

import sys

def quickSort1(list):
    pivot = list[0]
    left = []
    right = []
    for i in range(1, len(list)):
        if (list[i] > pivot):
            right.append(list[i])
        else:
            left.append(list[i])
    if len(left)>1:
        left = quickSort1(left)
    if len(right)>1:
       right = quickSort1(right)
    return left +[pivot] + right



if __name__ == '__main__':

    n = int(input().strip())
    unsorted = []
    for unsorted_i in range(n):
       unsorted_t = int(input())
       unsorted.append(unsorted_t)
    # your code goes here
    newsorted = quickSort1(unsorted)
    for item in newsorted:
        print(item)