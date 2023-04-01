# Python - Exceptions

Errors detected during _execution_ are called exceptions.

## Handling Exceptions

A `try...except` block is used.

```python
try:
        #some code here
except ExceptionType:
        #code to handle exception
```

* First, the `try` clause (the statement(s) between the try and except keywords) is executed.

* If no exception occurs, the `except` clause is skipped and execution of the try statement is finished.

* If an exception occurs during execution of the `try` clause, the rest of the clause is skipped. Then, if its type matches the exception named after the `except` keyword, the `except` clause is executed, and then execution continues after the try/except block.

* If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an _unhandled exception_ and execution stops with an error message.

A `try` statement may have more than one `except` clause, to specify handlers for different exceptions. **At most one handler will be executed.**  
Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple, for example:

```python
try:
        #some code
except (RuntimeError, TypeError, NameError):

```

## Tasks

* [0-safe_print_list.py](./0-safe_print_list.py) contains a function that prints x elements of a list.
  **Prototype:**

  ```python
  def safe_print_list(my_list=[], x=0):
  ```

* [1-safe_print_integer.py](./1-safe_print_integer.py) contains a function that prints an integer with `"{:d}".format()`.
  **Prototype:**

  ```python
  def safe_print_integer(value):
  ```
  
* [2-safe_print_list_integers.py](./2-safe_print_list_integers.py) contains a function that prints the first `x` elements of a list and only integers.
  **Prototype:**

  ```python
  def safe_print_list_integers(my_list=[], x=0):
  ```

* [3-safe_print_division.py](./3-safe_print_division.py) contains a function that divides 2 integers and prints the result.
  **Prototype:**

  ```python
  def safe_print_division(a, b):
  ```

* [4-list_division.py](./4-list_division.py) contains a function that divides element by element 2 lists, with the result being equal to 0 if the 2 elements cannot be divided.
  **Prototype:**

  ```python
  def list_division(my_list_1, my_list_2, list_length):
  ```

* [5-raise_exception.py](./5-raise_exception.py) contains a function that raises a type exception.
  **Prototype:**

  ```python
  def raise_exception():
  ```

* [6-raise_exception_msg.py](./6-raise_exception_msg.py) contains a function that raises a name exception with a message.
  **Prototype:**

  ```python
  def raise_exception_msg(message=""):
  ```
  
* [100-safe_print_integer_err.py](./100-safe_print_integer_err.py) contains a function that prints an integer using`"{:d}".format()` and returns `True` on success, otherwise returning `False` and printing to `stderr` the error preceded by `Exception:`
  **Prototype:**

  ```python
  def safe_print_integer_err(value):
  ```
  
* [101-safe_function.py](./101-safe_function.py) contains a function that executes a function safely, returning the result of the function otherwise returning `None` if something happens during the function execution and prints in `stderr` the error precede by `Exception:`
  **Prototype:**

  ```python
  def safe_function(fct, *args):
  ```

----

* [102-magic_calculation.py](./102-magic_calculation.py) contains a function

  ```python
  def magic_calculation(a, b):
  ```

  that deconstructs to the bytecode:

  ```bash
   3           0 LOAD_CONST               1 (0)
               3 STORE_FAST               2 (result)

   4           6 SETUP_LOOP              94 (to 103)
               9 LOAD_GLOBAL              0 (range)
              12 LOAD_CONST               2 (1)
              15 LOAD_CONST               3 (3)
              18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
              21 GET_ITER
         >>   22 FOR_ITER                77 (to 102)
              25 STORE_FAST               3 (i)

   5          28 SETUP_EXCEPT            49 (to 80)

   6          31 LOAD_FAST                3 (i)
              34 LOAD_FAST                0 (a)
              37 COMPARE_OP               4 (>)
              40 POP_JUMP_IF_FALSE       58

   7          43 LOAD_GLOBAL              1 (Exception)
              46 LOAD_CONST               4 ('Too far')
              49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
              52 RAISE_VARARGS            1
              55 JUMP_FORWARD            18 (to 76)

   9     >>   58 LOAD_FAST                2 (result)
              61 LOAD_FAST                0 (a)
              64 LOAD_FAST                1 (b)
              67 BINARY_POWER
              68 LOAD_FAST                3 (i)
              71 BINARY_TRUE_DIVIDE
              72 INPLACE_ADD
              73 STORE_FAST               2 (result)
         >>   76 POP_BLOCK
              77 JUMP_ABSOLUTE           22

  10     >>   80 POP_TOP
              81 POP_TOP
              82 POP_TOP
 
  11          83 LOAD_FAST                1 (b)
              86 LOAD_FAST                0 (a)
              89 BINARY_ADD
              90 STORE_FAST               2 (result)

  12          93 BREAK_LOOP
              94 POP_EXCEPT
              95 JUMP_ABSOLUTE           22
              98 END_FINALLY
              99 JUMP_ABSOLUTE           22
         >>  102 POP_BLOCK

  13     >>  103 LOAD_FAST                2 (result)
             106 RETURN_VALUE
  ```
