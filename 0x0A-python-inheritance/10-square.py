#!/usr/bin/python3
"""
This module contains a class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class Square inherits from a Rectangle
    """
    def __init__(self, size):
        """
        This method initializes the object's attributes when a class is create
d

        Args:
            size(int): Size of the square

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
