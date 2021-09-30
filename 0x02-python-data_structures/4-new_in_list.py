#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    z = len(my_list)
    new = my_list[:]
    if idx < 0 or idx >= z:
        return my_list
    new[idx] = element
    return new
