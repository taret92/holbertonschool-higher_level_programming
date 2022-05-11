#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    for i in matrix:
        new_matrix = map(matrix[i] * matrix[i])
    return new_matrix
