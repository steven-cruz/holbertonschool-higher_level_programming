#!/usr/bin/python3
''' function that return the number of lines of a text file '''


def number_of_lines(filename=""):
    count = 0
    with open(filename, encoding="utf-8") as f:  # open file (filename).
        for linea in f:  # browse the file.
            count += 1  # count the number of lines.
        return (count)  # return the number lines.
