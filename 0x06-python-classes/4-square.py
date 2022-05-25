#!/usr/bin/python3
"""Create a empty class"""


class Square:
    """square with size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getting size atributte"""
        return self.__size

    @size.setter
    def size(self, value):
        """adding value to size atribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the operation"""
        return self.__size ** 2
