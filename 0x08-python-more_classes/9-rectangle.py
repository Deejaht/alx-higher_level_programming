#!/usr/bin/python3
"""All about rectangles"""


class Rectangle:
    """defines a rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the class"""
        self.number_of_instances = self.number_of_instances + 1
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
                print_list.append(str(self.print_symbol))
            if i != self.__height - 1:
                print_list.append("\n")
        return "".join(print_list)

    def __repr__(self):
        """formal str representation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """runs when instance deleted"""
        self.number_of_instances = self.number_of_instances - 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the larger rectangle"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of a Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of a Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
