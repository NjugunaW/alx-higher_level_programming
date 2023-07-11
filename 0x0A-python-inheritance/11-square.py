#!/usr/bin/python3
"""
This module contains a class SQUARE
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class Square inherits from Rectangle
    """

    def __init__(self, size):
        """
        This method initializes the object's attributes when a class is create
d

        Args:
            size (int): Size of the square
        """

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        This method returns the square description

        :return:
        <width>/<height>
        """

        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        Computes the area of the Square
        """
        return self.__size ** 2
