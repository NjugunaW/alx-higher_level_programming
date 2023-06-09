#!/usr/bin/python3
"""A class that defines a Rectangle."""


class Rectangle:
    """Defines a rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """__init__ is called when a new object is created

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Should print the rectangle with the character #.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for l in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Should return a string representation of the rectangle to be able to recreate a new instance"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """When an instance of Rectangle is delete"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
