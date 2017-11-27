#!/bin/python3

import string
if __name__ == '__main__':

    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    output = []
    for letter in s:
        if letter in string.ascii_letters:
            if letter.islower():
                index = string.ascii_lowercase.index(letter)
            elif letter.isupper():
                index = string.ascii_uppercase.index(letter)

            index = (index + k)%26

            if letter.islower():
                output.append(string.ascii_lowercase[index])
            elif letter.isupper():
                output.append(string.ascii_uppercase[index])
        else:
            output.append(letter)
    print("".join(output))
