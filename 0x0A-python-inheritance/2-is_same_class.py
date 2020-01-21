#!/usr/bin/python3
''' function that return True if the object is exactly '''


def is_same_class(obj, a_class):
    ''' verify if the instance is the same '''

    return issubclass(a_class, type(obj))
