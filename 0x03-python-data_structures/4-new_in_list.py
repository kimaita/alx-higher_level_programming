def new_in_list(my_list, idx, element):
    """_summary_

    Args:
        my_list (_type_): _description_
        idx (_type_): _description_
        element (_type_): _description_
    """
    new_list = my_list.copy()

    if not (idx < 0 or idx >= len(my_list)):
        new_list[idx] = element
    return new_list
