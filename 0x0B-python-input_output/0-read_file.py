#!/usr/bin/python3
''' function that reads a text file (UTF8) '''


def read_file(filename=""):
    ''' file to read '''

    with open(filename, encoding='utf-8') as f:
        for linea in f:
            print(linea, end='')
