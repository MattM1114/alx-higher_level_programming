#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def find(element):
        return element if element != search else replace
    return list(map(find, my_list))
