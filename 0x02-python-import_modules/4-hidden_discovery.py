#!/usr/bin/python3
mod = __import__('hidden_4')

if __name__ == "__main__":
    for name in dir(mod):
        if not name.startswith('__'):
            print(name)
