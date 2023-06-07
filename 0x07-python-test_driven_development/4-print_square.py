#!/usr/bin/python3
"""print square module"""
import doctest


def print_square(size):
    """print square function"""
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)


if __name__ == '__main__':
    doctest.testfile("./tests/4-print_square.txt")