# Python Hello World

## Python Script/Code running

An introduction to Python with tasks on script and code execution:

* [0-run](./0-run): shell script to execute a python script
* [1-run_inline](./1-run_inline): shell script to run python code

## Python Scripting

An introduction to Python scripts with an emphasis on the usage of Python's `print()` function and formatting with [f-strings](https://realpython.com/python-f-strings/)

* [2-print.py](./2-print.py) prints `"Programming is like building a multilingual puzzle`, followed by a new line
* [3-print_number.py](./3-print_number.py) prints an integer followed by `Battery Street` and a new line
* [4-print_float.py](./4-print_float.py) prints a float with a 2-digit precision followed by a new line
* [5-print_string.py](./5-print_string.py) prints a string 3 times then a new line then the first 9 characters of the string followed by a new line.  
Example for a string 'Holberton School':

  ```bash
  ./5-print_string.py 
  Holberton SchoolHolberton SchoolHolberton School
  Holberton
  ```

* [6-concat.py](./6-concat.py) prints a concatenation of two strings
* [7-edges.py](./7-edges.py) prints the first 3, last 2 and middle(without first and last) characters of a string  
Example for a string 'Holberton':

  ```bash
  ./7-edges.py
  First 3 letters: Hol
  Last 2 letters: on
  Middle word: olberto 
  ```

* [8-concat_edges.py](./8-concat_edges.py) prints `object-oriented programming with Python`, followed by a new line.
* [9-easter_egg.py](./9-easter_egg.py): a Python script(<=98 characters) that prints “The Zen of Python”, by TimPeters
* [100-write.py](./100-write.py) uses `write()` from the `sys` module to print `and that piece of art is useful - Dora Korpar, 2015-10-19` to `stderr`
* [101-compile](./101-compile) compiles a python script into a similarly named `.pyc` file
* [102-magic_calculation.py](./102-magic_calculation.py) contains a function(`magic_calculation()`) thats does the same as the bytecode:

  ```bash
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
  ```

## Technical interview preparation

[10-check_cycle.c](./10-check_cycle.c) contains a C function that checks if a singly linked list has a cycle in it

  **Prototype:**

  ```C
  int check_cycle(listint_t *list);
  ```

  **Return:** 0 if there is no cycle, 1 if there is a cycle

[10-linked_lists.c](./10-linked_lists.c) contains functions for adding nodes to a linked list, freeing and printing a linked list  
[10-main.c](./10-main.c) contains `main()` and is used to check the written function

### Compilation

```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle && ./cycle
```
