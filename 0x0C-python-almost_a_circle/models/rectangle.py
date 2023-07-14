#!/usr/bin/python3

""""
This module has a class Rectangle that inherits from Base
"""
from base import Base

class Rectangle(Base):
    """
    This function defines a class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is a class constructor
        Args:
            width:
            height:
            x:
            y:
            id:
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """
            This is the width attribute of the rectangle

            Returns:
                value of width attribute
            """
        @property
        def height(self):
            """
            This is the height attribute of the rectangle
            Args:
                self:

            Returns:

            """


        def area(self):
            """
            This function computes the area of a rectangle

            Returns:
                The area value of the Rectangle
            """
            return self.width * self.height
