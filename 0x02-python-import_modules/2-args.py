#!/usr/bin/python3
import sys

i = 1
args = sys.argv[1:]
argc = len(args)
if __name__ == "__main__":
    if argc:
        print('{} {}:'.format(argc, 'arguments' if argc > 1 else 'argument'))
        for arg in args:
            print(f"{i}: {arg}")
            i += 1
    else:
        print('0 arguments.')
