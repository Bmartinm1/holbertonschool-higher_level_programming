#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        if i == 8 and x == 9:
            print("89")
        elif i < x:
            print("{:d}{:d}, ".format(i, x), end="")
