#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zero = 0
    tupa = list(tuple_a)
    tupb = list(tuple_b)
    len_a = len(tupa)
    len_b = len(tupb)
    while len_a < 2:
       tupa.append(zero)
       len_a += 1
    while len_b < 2:
       tupb.append(zero)
       len_b += 1
    x = tupa[0] + tupb[0]
    z = tupa[1] + tupb[1]
    return x, z
