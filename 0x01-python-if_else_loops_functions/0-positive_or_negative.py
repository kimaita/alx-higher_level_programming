#!/usr/bin/python3
import random
number = random.randint(-10, 10)
is_what = ''
if number == 0:
    is_what = 'zero'
elif number > 0:
    is_what = 'positive'
else:
    is_what = 'negative'
print(f"{number} is {is_what}")
