#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list
    (only once for each integer).

    Args:
        my_list (list, optional): _description_. Defaults to [].
    """
    sum = 0
    if my_list:
        ints = set(my_list)
        for i in ints:
            sum += i
    return sum
