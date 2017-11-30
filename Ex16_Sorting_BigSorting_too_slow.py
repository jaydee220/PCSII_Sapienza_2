#!/bin/python3

import sys


# def quickSort1(list):
#     pivot = list[0]
#     left = []
#     right = []
#     for i in range(1, len(list)):
#         if (list[i] > pivot):
#             right.append(list[i])
#         else:
#             left.append(list[i])
#     if len(left) > 1:
#         left = quickSort1(left)
#     if len(right) > 1:
#         right = quickSort1(right)
#     return left + [pivot] + right


def SortingBigIntegers(arr, n):
    # Direct sorting using lamda operator
    # and length comparison
    return arr.sort(key=lambda x: (len(x), x))


if __name__ == '__main__':

    n = int(input().strip())
    unsorted = []
    for unsorted_i in range(n):
       unsorted.append(input())
    # your code goes here
    SortingBigIntegers(unsorted,n)
    for item in unsorted:
        print(item)