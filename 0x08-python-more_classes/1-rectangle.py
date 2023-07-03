#!/usr/bin/python3
"""Reps a rectangle"""

class Rectangle:
    """ defines a rectangle"""

    def __init__(self, width=0, height=0):
        """__init__

        __init__ is called when a new object is created.

        Args:
            width(int): Width of rectangle
            height(int): Height of rectangle
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """Retrieves width of rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """Retrieves height of rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

