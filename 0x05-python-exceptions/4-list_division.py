#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    If 2 elements can’t be divided, the division result should be
    equal to 0

    Args:
        my_list_1: the first list
        my_list_2: the second list
        list_length: number of divisions to perform
    Returns:
        a new list (length = `list_length`) with all divisions
    """
    i = 0
    result = []
    while i < list_length:
        try:
            quotient = my_list_1[i]/my_list_2[i]
        except TypeError:
            print('wrong type')
            quotient = 0
        except ZeroDivisionError:
            print('division by 0')
            quotient = 0
        except IndexError:
            print('out of range')
            quotient = 0
        finally:
            result.append(quotient)
            i += 1
    return result
