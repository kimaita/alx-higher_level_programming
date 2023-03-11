#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds the first two elements of two tuples

    Args:
        tuple_a: First tuple. Defaults to ().
        tuple_b: Second tuple. Defaults to ().

    Returns:
        sum of the respective first and second elements
        of tuple_a and tuple_b
    """
    len_a, len_b = len(tuple_a), len(tuple_b)
    a_0 = tuple_a[0] if len_a else 0
    a_1 = tuple_a[1] if len_a > 1 else 0
    b_0 = tuple_b[0] if len_b else 0
    b_1 = tuple_b[1] if len_b > 1 else 0

    return (a_0 + b_0, a_1 + b_1)
