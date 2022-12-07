#!/usr/bin/python3

# element = e
def uniq_add(my_list=[]):
    number = 0
    for e in set(my_list):
        number += e
    return number
