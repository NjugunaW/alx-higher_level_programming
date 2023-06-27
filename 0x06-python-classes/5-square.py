#!/usr/bin/python3

class Square:
    """ Defines a Square Class"""

    def __init__(self, size):
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
        """Return the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
