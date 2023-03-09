#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculate(a: int, b: int, operator):
    if operator == '+':
        return add(a, b)
    if operator == '-':
        return sub(a, b)
    if operator == '*':
        return mul(a, b)
    if operator == '/':
        return div(a, b)


if __name__ == "__main__":
    args = sys.argv[1:]
    argc = len(args)
    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif args[1] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        result = calculate(int(args[0]), int(args[2]), args[1])
        print('{} {} {} = {}'.format(args[0], args[1], args[2], result))
