#!/usr/bin/python3

"""
This module contains an empty class
"""

BaseGeometry = __import__ ('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from  Basegeometry
    """


    def __init__(self, width, height):
        """
        This method is called when a new object is created
        Args:
        :width:
        :height:
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

