#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces the element at an index in a list

    No modification to the list happens for an index that is
    out of bounds or negative

    Args:
        my_list: list of elements
        idx: index of element to replace
        element: element to replace with

    Returns:
        the modified list
    """
    if not (idx < 0 or idx >= len(my_list)):
        my_list[idx] = element
    return my_list
