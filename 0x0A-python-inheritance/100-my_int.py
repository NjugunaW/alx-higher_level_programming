#!/usr/bin/python3

class MyInt(int):
    """
    A class MyInt that inherits from int
    """
    def __eq__(self, num):
        """
        Used to implement the equality comparison between objects of a class

        Args:
            num (int): an inputed integer

        Returns:
            Boolean value showing the equality
        """
        return (int(self) != num)

    def __ne__(self, num):
        """
        Used to implement inequality comparison between objects of a class

        Args:
            num (int): an inputed integer

        Returns:
            Boolean value showing the inequality
        """
        return (int(self) == num)
