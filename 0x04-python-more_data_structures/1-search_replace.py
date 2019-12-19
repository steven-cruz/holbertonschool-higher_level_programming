#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = my_list[:]
    for n, i in enumerate(n_list):
        if i == search:
            n_list[n] = replace
    return (n_list)
