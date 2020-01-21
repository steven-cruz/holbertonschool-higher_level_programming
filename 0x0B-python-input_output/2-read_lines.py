#!/usr/bin/python3
''' function that reads n lines of a text file '''


def read_lines(filename="", nb_lines=0):
    count = 0
    with open(filename, encoding="utf-8") as f:
        for linea in f:
            count += 1
            print(linea, end="")
            if nb_lines == count:
                break
