#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for item in my_list:
        if item == search:
            newList.append(replace)
        else:
            newList.append(item)
    return newList
