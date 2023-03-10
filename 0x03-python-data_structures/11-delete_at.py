def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list

    Args:
        my_list: The list to remove an item from. Defaults to [].
        idx: index of item to remove. Defaults to 0.

    Returns:
        the modified list or
        the same list if idx is out of range or negative
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list
