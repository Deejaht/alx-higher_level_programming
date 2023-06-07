#!/usr/bin/python3
"""Add integer module"""
import doctest


def add_integer(a, b=98):
    """add_integer function"""
    if (isinstance(a, (int, float)) is False):
        raise TypeError("a must be an integer")
    if (isinstance(b, (int, float)) is False):
        raise TypeError("b must be an integer")
    if (type(a) is float):
        a = float(a)
    if type(b) is float:
        b = float(b)
    return a + b


if __name__ == '__main__':
    doctest.testfile("../tests/0-add_integer.txt")
