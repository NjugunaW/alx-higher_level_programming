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
        This method gets the width attribute of the rectangle

        Returns:
            value of width attribute
        """

        return self.__width


        @property
        def height(self):
            """
            This method gets the height attribute of the rectangle

            Returns:
                value of height attribute
            """
            return self.__height
        @property
        def x(self):
            """
            This method gets the horizontal attribute of the rectangle

            Returns:
                value of x attribute
            """
            return self.__x
        @property
        def y(self):
            """
            This method gets the vertical attribute of the rectangle

            Returns:
                value of y attribute
            """
            return self.__y

        @width.setter
        def width(self, width):
            """
            This method sets the width of the rectangle
            Args:
                width: The width of the rectangle

            Raises:
                TypeError: width must be an integer
                ValueError: width must be > 0
            """
            if type(width) != int:
                raise TypeError ('width must be an integer')
            elif width < 1:
                raise ValueError('width must be > 0')

            self.__width = width
        @height.setter
        def height(self, height):
            """
            This method sets the height of the rectangle

            Args:
                height: height of the rectangle

            Raises:
                TypeError: height must be an integer
                ValueError: height must be > 0
            """
            if type(height) != int:
                raise TypeError('height must be an integer')
            elif height < 1 :
                raise ValueError('height must be > 0')

            self.__height = height

        @x.setter
        def x(self, x):
            """
            This method sets the x value of the rectangle

            Args:
                x: horizontal value rectangle

            Raises:
                TypeError: x must be an integer
                ValueError: x must be >= 0
            """
            if type(x) != int:
                raise TypeError('x must be an integer')
            elif x < 0:
                raise ValueError('x must be >= 0')

            self.__x = x

        @y.setter
        def y(self, y):
            """
            This method sets the y value of the rectangle

            Args:
                y: vertical value rectangle

            Raises:
                TypeError: y must be an integer
                ValueError: y must be >= 0
            """
            if type(y) != int:
                raise TypeError('y must be an integer')
            elif y < 0:
                raise ValueError('y must be >= 0')

            self.__y = y

        def area(self):
            """
            This function computes the area of a rectangle

            Returns:
                The area value of the Rectangle
            """
            return self.__width * self.__height

        def display(self):
            """
            This method prints the Rectangle instance with the character #
            in stdout.
            """
            for m in range(self.__y):
                print()
            for m in range(self.__height):
                for w in range(self.__x):
                    print(' ', end='')
                for w in range(self.__width):
                    print('#', end='')
                print()

        def __str__(self):
            """
            This method returns
            [Rectangle] (<id>) <x>/<y> - <width>/<height>

            Returns:
            """
            return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(self.id, self.x, self.y, self.width, self.height)

        def update(self, *args, **kwargs):
            """
            This method updates a class by assigning a key/value argument to its attributes
            Args:
                args:
                kwargs:
            """
            attr_bts = ('id', 'width', 'height', 'x', 'y')
            for key, val in zip(attr_bts, args):
                setattr(self, key, val)
            if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
                for key, val in kwargs.items():
                    if key in attr_bts:
                        setattr(self, key, val)

    def to_dictionary(self):
        """
        This method returns the dictionary representation of a Rectangle
        """
        output = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return output




