#!/bin/python3

import sys

s = input().strip()
word = 1
for letter in s:
    if letter.isupper():
        word += 1
print(word)
