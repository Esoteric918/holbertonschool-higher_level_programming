#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    z = []
    for r in matrix:
        x = list(map(lambda x: x**2, r))
        z.append(x)
    return z