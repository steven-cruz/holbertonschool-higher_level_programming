#!/usr/bin/python3
''' Class Base '''

import json


class Base:
    '''Base Class with private attributes'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Instantiation of id for Base Class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''Method that returns the JSON string representation of function'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
