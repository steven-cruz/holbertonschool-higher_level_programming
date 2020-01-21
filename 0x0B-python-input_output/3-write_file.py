#!/usr/bin/python3
''' writes a string to a text file, return the number of charachers '''


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
