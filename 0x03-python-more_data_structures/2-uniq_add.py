#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = set(my_list)
    j = 0
    for i in x:
        j += i
    return j
