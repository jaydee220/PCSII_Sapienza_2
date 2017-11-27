#!/bin/python3
from datetime import datetime


def timeConversion(s):
    input1  = datetime.strptime(s,"%I:%M:%S%p")
    return input1.strftime("%H:%M:%S")

if __name__ == '__main__':

    s = input().strip()
    result = timeConversion(s)
    print(result)
