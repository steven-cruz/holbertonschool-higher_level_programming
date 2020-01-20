#!/usr/bin/python3
''' class MyList that inherits from list '''


class MyList(list):
    ''' MyList class inherits from the parent list class'''


    def print_sorted(self):  # public instance method
        print(sorted(self))  # print the list, but sorted(ascending sort)
