#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value.

    Args:
        a_dictionary:the dictionary of scores
    Returns:
        Key with the largest integer value or
        None if no score found
    """
    if not a_dictionary:
        return None
    sorted_k = sorted(a_dictionary.keys(),
                      reverse=True,
                      key=lambda x: a_dictionary.get(x))
    best = sorted_k[0]
    return best
