#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sdc = sorted(a_dictionary.keys())
    for k in sdc:
        print("{}: {}".format(k, a_dictionary[k]))