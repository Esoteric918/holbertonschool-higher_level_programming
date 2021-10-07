#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    res = 0.0
    s_list = list(t[0] * t[1] for t in my_list)
    w_list = (t[1] for t in my_list)
    res = sum(s_list) / sum(w_list)
    return res
