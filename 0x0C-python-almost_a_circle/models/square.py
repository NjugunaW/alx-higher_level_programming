#!/usr/bin/python3
""""
This module has a class Square that inherits from Rectangle
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    This is a class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is a class constructor
        Args:
            size:
            x:
            y:
            id:
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This method returns a string
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        This method sets the size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        This method sets the size of the square
        Args:
            size: Size of square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        This method updates the Square Class
        Args:
            *args:
            **kwargs:
        """
        arg_mnt = len(args)
        new_kwarg = len(kwargs)
        attr_bts = ['id', 'size', 'x', 'y']

        if arg_mnt > 8:
            arg_mnt = 8

        if arg_mnt > 0:
            for m in range(arg_mnt):
                setattr(self, attr_bts[m], args[m])
        elif new_kwarg > 0:
            for b, h in kwargs.items():
                if b in attr_bts:
                    setattr(self, b, h)

    def to_dictionary(self):
        """
        This method returns the dictionary representation of a Rectangle
        """
        return{
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

