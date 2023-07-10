#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class Square that inherits from a Rectangle
    """
    def __init__(self, size):
        """
        Called when an new object is created

        Args:
            size(int): Size of the square

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
