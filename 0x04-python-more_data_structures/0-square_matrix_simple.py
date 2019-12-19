#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        n_matrix = []
        for rows in matrix:
            n_matrix.append([n ** 2 for n in rows])
        return n_matrix
