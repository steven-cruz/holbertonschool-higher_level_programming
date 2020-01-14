#!/usr/bin/python3


'''
    2-matrix_divided function

    function that divides all elements of a matrix.
'''


def matrix_divided(matrix, div):
    ''' python function that divide a matrix by variable '''

    listError = "matrix must be a matrix (list of lists) of integers/floats"
    ''' check if matrix is a list '''
    if type(matrix) is not list:
        raise TypeError(listError)

    ''' check if rows in matrix list '''
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(listError)

    ''' check if length of rows are the same '''
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    ''' check to see if div is zero '''
    if div == 0:
        raise ZeroError("division by zero")

    ''' check if div is int or float '''
    for rows in matrix:
        for items in rows:
            if not isinstance(items, (int, float)):
                raise TypeError(listError)

    ''' python funtion to divide elements of a matrix '''

    new = []
    for rows in matrix:
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        else:
            new.append([round((items / div), 2) for items in rows])
    return new
