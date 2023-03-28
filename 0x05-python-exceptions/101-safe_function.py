#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        `fct`: Pointer to the function
    Returns:
        result of the function or `None` if something happens during
        the function execution
    """
    try:
        return fct(*args)
    except Exception as e:
        print('Exception: {}'.format(e), file=sys.stderr)
        return None
