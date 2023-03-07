#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number != 0:
    last_digit *= number//abs(number)  # retrieve the sign
is_what = ''
if last_digit > 5:
    is_what = 'greater than 5'
elif last_digit == 0:
    is_what = '0'
else:
    is_what = 'less than 6 and not 0'
print(f"Last digit of {number} is {last_digit} and is {is_what}")
