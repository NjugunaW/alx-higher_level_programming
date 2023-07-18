#!/usr/bin/python3
"""This module has a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """This function defines a class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This method initializes a class constructor.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """This method gets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This method gets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This method gets the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This method gets the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method computes the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """This method prints the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            idx = 0
            for arg_mnt in args:
                if idx == 0:
                    if arg_mnt is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg_mnt
                elif idx == 1:
                    self.width = arg_mnt
                elif idx == 2:
                    self.height = arg_mnt
                elif idx == 3:
                    self.x = arg_mnt
                elif idx == 4:
                    self.y = arg_mnt
                idx += 1

        elif kwargs and len(kwargs) != 0:
            for mn, cm in kwargs.items():
                if mn == "id":
                    if cm is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = cm
                elif mn == "width":
                    self.width = cm
                elif mn == "height":
                    self.height = cm
                elif mn == "x":
                    self.x = cm
                elif mn == "y":
                    self.y = cm

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)