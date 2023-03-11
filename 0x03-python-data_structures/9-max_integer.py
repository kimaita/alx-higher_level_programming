#!/usr/bin/python3
def max_integer(my_list=[]):
    """Returns the biggest integer of a list

    Args:
        my_list: _description_. Defaults to [].
    """
    if not len(my_list):
        return None

    my_list.sort(reverse=True)
    list_max = my_list[0]
    return list_max
