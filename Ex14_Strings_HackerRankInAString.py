#!/bin/python3

import sys
if __name__ == '__main__':


    word = "hackerrank"
    check = True

    q = int(input().strip())
    for a0 in range(q):
        count = 0
        s = input().strip()
        if len(s)< len(word):
            print ("NO")
            break

        for i in range(len(s)):
            if count < len(word) and s[i]==word[count]:
                x = word[count]
                count+=1
        if count !=10:
            print("NO")
        else:
            print("YES")



