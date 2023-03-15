#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element in a list
    by another in a new list

    Args:
        my_list: the original list
        search: element to find and replace
        replace: element to replace with

    Returns:
        A new list with search replaced by replace
    """
    return [replace if x == search else x for x in my_list]
