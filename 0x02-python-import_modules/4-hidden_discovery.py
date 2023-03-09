#!/usr/bin/python3
mod = __import__('hidden_4')
for name in dir(mod):
    if not name.startswith('__'):
        print(name)
