#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    a class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """"
        Called when a new object is created

        Args:
            size (int): Size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        should return, the square description

        Returns:
        <width>/<height>
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        Computes the area of the Square
        """
        return self.__size ** 2
