#!/usr/bin/python3
"""All about rectangles"""


class Rectangle:
    """defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """initializes the class"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Get the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """informal str representation"""
        print_list = []
        if (self.__width == 0 or self.__height == 0):
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print_list.append("#")
            if i != self.__height - 1:
                print_list.append("\n")
        return "".join(print_list)

