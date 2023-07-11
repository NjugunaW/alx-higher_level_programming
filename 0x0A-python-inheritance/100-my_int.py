#!/usr/bin/python3
"""
This module contains a class that inherits from int
"""

class MyInt(int):
    """
    This class inherits from int
    """

    def __eq__(self, num):
        """
        This function is used to implement the 
        equality comparison between objects of a class

        Args:
            num (int): an inputed integer

        Returns:
            Boolean value showing the equality
        """

        return (int(self) != num)

    def __ne__(self, num):
        """
        This function is used to implement
        inequality comparison between objects of a class

        Args:
            num (int): an inputed integer

        Returns:
            Boolean value showing the inequality
        """

        return (int(self) == num)
