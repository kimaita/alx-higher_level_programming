#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    prod, n = 0, 0
    for tup in my_list:
        prod += tup[0] * tup[1]
        n += tup[1]
    return prod/n
