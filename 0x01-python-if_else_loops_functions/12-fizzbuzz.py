#!/usr/bin/python3
def fizzbuzz():
    """Prints 1 to 100

    Prints Fizz for multiples of 3,
    Buzz for multiples of 5,
    FizzBuzz for multiples of both 3 and 5
    """
    for i in range(1, 101):
        if not (i % 3) and not (i % 5):
            print('FizzBuzz', end=' ')
        elif not i % 3:
            print('Fizz', end=' ')
        elif not i % 5:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')
