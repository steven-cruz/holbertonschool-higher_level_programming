#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) <= 0:
        return (0)
    n_list = set(my_list)
    sum1 = 0
    for i in n_list:
        sum1 += i
    return(sum1)
