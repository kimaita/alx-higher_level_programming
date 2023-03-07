#!/usr/bin/python3
for letter in range(ord('a'), ord('z')):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print(chr(letter), end='')
