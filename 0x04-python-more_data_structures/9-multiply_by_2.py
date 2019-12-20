#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dictionary = a_dictionary.copy()
    for value in copy_dictionary:
        copy_dictionary[value] *= 2
    return(copy_dictionary)
