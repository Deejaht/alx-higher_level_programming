#!/usr/bin/python3
"""matrix divided module"""
import doctest


def matrix_divided(matrix, div):
    """matrix divided function"""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) is not list or len(i) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for inner_list in matrix:
        for i in inner_list:
            if (isinstance(i, (int, float)) is False):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    row_size = 0
    if len(matrix) > 0:
        row_size = len(matrix[0])
    for i in matrix:
        if len(i) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if (isinstance(div, (int, float)) is False):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    for inner_list in matrix:
        new_sublist = []
        for num in inner_list:
            new_sublist.append(round(num/div, 2))
        new_list.append(new_sublist)

    return new_list


if __name__ == '__main__':
    doctest.testfile("../tests/2-matrix_divided.txt")
