#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves the element at the given index

    Args:
                my_list: list containing elements

        Returns:
                element at index idx of my_lisr or

                None if idx is out of range or negative
    """
    if idx >= len(my_list) or idx < 0:
        return None
    return my_list[idx]
