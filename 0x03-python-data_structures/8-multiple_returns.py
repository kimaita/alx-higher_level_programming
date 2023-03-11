#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns the length of sentence,
    and its first character or None if empty

    Args:
        sentence: string to extract length and first character

    Returns:
        length of sentence, the first character(or None)
    """
    len_s = len(sentence)
    return (len_s, sentence[0] if len_s else None)
