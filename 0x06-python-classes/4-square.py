#!/usr/bin/python3

class Square:
    """Defines a Class Square"""

    def __init__(self, size=0):
        """__init__ is called when a new instance of a class is created
        Attributes:
            size (:obj: `int`): Size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """returns the current square area."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
