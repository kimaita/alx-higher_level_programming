def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 and
    returns a list of True/False values accordingly

    Args:
        my_list (list, optional): . Defaults to [].
    """
    return [False if i % 2 else True for i in my_list]
