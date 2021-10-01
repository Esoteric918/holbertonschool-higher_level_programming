#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    largest = 0
    for x in range(0, len(my_list)):
        if(my_list[x] > largest):
            largest = my_list[x]
    return largest
