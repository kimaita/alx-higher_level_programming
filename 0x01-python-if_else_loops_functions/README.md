# Python - if/else, loops, functions

An introduction to conditionals and looping in Python together with function declaration, definition and usage.

## Conditional statements

Use of `if`, `if...else`, `if...elif...else` in Python

* [0-positive_or_negative.py](./0-positive_or_negative.py) prints a number and:  
  *is positive* if number > 0  
  *is zero* if number is zero  
  *is negative* if number < 0  
  **Format:** `{number} is {positive}`

* [1-last_digit.py](./1-last_digit.py) prints a number, its last digit and  
  *is greater than 5* if last digit > 5  
  *is 0* if last digit is 0  
  *is less than 6 and not 0* if the last digit is less than 6 and not 0  
  **Format:** `Last digit of {number} is {last_digit} and {is less than 6 and not 0}`

## Looping

Use of `while` and `for` loops in Python.  
`break`, `continue`, `else` and `pass` statements in Python loops.  
`range()` in Python

* [2-print_alphabet.py](./2-print_alphabet.py) prints the ASCII alphabet, in lowercase, not followed by a new line  
**Output:**

  ```bash
  abcdefghijklmnopqrstuvwxyz
  ```

* [3-print_alphabt.py](./3-print_alphabt.py) prints the ASCII alphabet, in lowercase, except for *q* and *e*, not followed by a new line  
**Output:**

  ```bash
  abcdfghijklmnoprstuvwxyz
  ```

* [4-print_hexa.py](./4-print_hexa.py) prints all numbers from 0 to 98 in decimal and in hexadecimal  
**Output:**  

  ```bash
  0 = 0x0  
  ...  
  98 = 0x62  
  ```

* [5-print_comb2.py](./5-print_comb2.py) prints comma-separated, two-digit numbers from 0 to 99  
**Output:**

  ```bash
  00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
  ```

* [6-print_comb3.py](./6-print_comb3.py) prints all possible different combinations of two digits with the two digits being different and the combo being the smallest possible combination in ascending order  
**Output:**

  ```bash
  01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
  ```

* [100-print_tebahpla.py](./100-print_tebahpla.py) prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase, not followed by a new line.  
 **Output:**

  ```bash
  zYxWvUtSrQpOnMlKjIhGfEdCbA
  ```

## Functions

Function usage  
`return` and `None` returns  
Variable scopes  

* [7-islower.py](./7-islower.py) contains a function that checks for lowercase character.  
**Prototype:**

  ```python
  def islower(c):
  ```

  **Return:**  
  `True` if the character is lowercase  
  `False` otherwise

* [8-uppercase.py](./8-uppercase.py) contains a function that prints a string in uppercase followed by a new line  
**Prototype:**

  ```python
  def uppercase(str):
  ```

* [9-print_last_digit.py](./9-print_last_digit.py) contains a function that prints and returns the last digit of a number.  
**Prototype:**

  ```python
  def print_last_digit(number):
  ```

  **Return:** value of the last digit

### Arithmetic operators

* [10-add.py](./10-add.py) contains a function that returns the result of the addition of two integers
**Prototype:**

  ```python
  def add(a, b):
  ```

  **Return:** value of `a + b`

* [11-pow.py](./11-pow.py) contains a function that returns the value of a to the power of b  
**Prototype:**

  ```python
  def pow(a, b):
  ```

  **Return:** value of `a ^ b`

* [12-fizzbuzz.py](./12-fizzbuzz.py) contains a function that prints the numbers from 1 to 100 separated by a space but prints:  
 `Fizz` for multiples of 3  
 `Buzz` for multiples of 5  
 `FizzBuzz` for multiples of both 3 and 5  
 **Prototype:**

  ```python
  def fizzbuzz():
  ```

  **Output:**

  ```bash
  1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz
  ```

* [101-remove_char_at](./101-remove_char_at.py) contains a funtion that creates a copy of a string, removing the character at the position n (not the Python way, the “C array index”)  
**Prototype:**

  ```python
  def remove_char_at(str, n):
  ```

* [102-magic_calculation.py](./102-magic_calculation.py) contains a funtion that does the same as the bytecode:  

  ```bash
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
  ```

  **Prototype:**

  ```python
  def magic_calculation(a, b, c):
  ```
