#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i:
            print("{}{}".format(i, j), end="\n" if i == 8 else", ")
