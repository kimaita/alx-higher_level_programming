#!/usr/bin/python3
"""A module with stdin reading funtionality"""
import sys


def print_results(size, codes):
    print(f"File size: {size}")
    for code in sorted(codes.items()):
        print(f'{code[0]}: {code[1]}')


if __name__ == "__main__":
    i = 0
    file_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            i += 1
            parts = line.split()
            code = parts[-2]
            if code in status_codes:
                status_codes[code] += 1
            else:
                status_codes[code] = 1
            file_size += int(parts[-1])
            if not i % 10:
                print_results(file_size, status_codes)
    except KeyboardInterrupt as e:
        print_results(file_size, status_codes)
        raise
