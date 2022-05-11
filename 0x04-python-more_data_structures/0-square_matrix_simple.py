#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for new in matrix:
        new_matrix.append([i**2 for i in new])
    return new_matrix
