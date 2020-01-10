#!/usr/bin/python3
''' 3-square.py: Public instance method '''


class Square:
    ''' Creates Square type '''
    def __init__(self, size=0):
        ''' initializes square with size'''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        ''' defines the area of a squere '''
        return self.__size * self.__size
