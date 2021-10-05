#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for k, v in a_dictionary.items():
        v = v * 2
        one_dict = {k: v}
        new_dict.update(one_dict)
    return new_dict
