#!/usr/bin/python3

"""
This module contains an empty class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        This method initializes the object's attributes when a class is created
        Args:
            width (int): Width of the rectangle
            height (int): height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        This method returns the rectangle's description

        :return:

        """

        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """
        This method computes the area of the rectangle
        
        :return:
        """

        return self.__width * self.__height
