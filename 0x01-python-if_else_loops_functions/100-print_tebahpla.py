#!/usr/bin/python3
n = ord('z')
while n >= ord('a'):
    print('{:c}{:c}'.format(n, (n-1)-32), end='')
    n-=2
    
