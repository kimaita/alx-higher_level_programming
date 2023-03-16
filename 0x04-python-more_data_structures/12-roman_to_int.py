#!/usr/bin/python3
rom_arabic = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer.

    Args:
        roman_string:the Roman numeral to convert

    Returns:
        integer equivalent of roman_string or
        0 if roman_string not a string or is None
    """
    num = 0
    if isinstance(roman_string, str):
        if len(roman_string) == 1:
            return rom_arabic.get(roman_string)
        else:
            for i in range(1, len(roman_string)):
                num += action(roman_string[i-1], roman_string[i])
                i += 2
            return num
    else:
        return None


def action(x, y):
    if rom_arabic[x] >= rom_arabic[y]:
        return rom_arabic[x] + rom_arabic[y]

    return rom_arabic[y] - rom_arabic[x]
