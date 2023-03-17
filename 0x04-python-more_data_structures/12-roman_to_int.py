#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer.

    Args:
        roman_string:the Roman numeral to convert

    Returns:
        integer equivalent of roman_string or
        0 if roman_string not a string or is None
    """
    num = 0
    rom_arabic = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    if isinstance(roman_string, str):
        roman_string = roman_string.upper()
        if len(roman_string) == 1:
            return rom_arabic.get(roman_string)
        else:
            for i in range(0, len(roman_string)-1):
                right = rom_arabic.get(roman_string[i+1])
                val = rom_arabic.get(roman_string[i])
                if val < right:
                    num -= val
                else:
                    num += val
            num += right
            return num
    else:
        return None
