#!/usr/bin/python3
'''
   * function that appends a string at the end of a text file.
   * returns the numer of characters addes.
'''


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as f:  # a created file and add
        return f.write(text)
