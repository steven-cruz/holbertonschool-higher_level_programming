#!/bin/usr/python3
''' class Square '''

from models.rectangle import Rectangle


class Square(Rectangle):
    ''' this class inherits from the rectangle class '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' instantiation of Square attributes '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' set the property of width '''
        return self.height

    @size.setter
    def size(self, value):
        ''' method to set size '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.height = value

    def update(self, *args, **kwargs):
        '''Set up args for rectangle'''
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        '''Method to return dictionary representation of square'''
        dic = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dic
