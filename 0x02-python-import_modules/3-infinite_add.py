#!/usr/bin/python3
import sys

args = sys.argv[1:]
sum = 0
if __name__ == "__main__":
    for arg in args:
        sum += int(arg)
    print(sum)
