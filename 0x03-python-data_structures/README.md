# Python - Data Structures: Lists, Tuples

An introduction to lists and tuples in Python.  
Both lists and tuples are:

* _compound_ data types meaning they group together other values.

* Python _iterables_ meaning they are objects capable of returning their members one at a time.

* Python _sequence_ types meaning they are iterables that allow integer indexing

|Property|List|Tuple|
|----|---|--|
|Mutability|Mutable| Immutable|
|Bracketing|square bracketed| round brackets|
|Creation|`li = [1, 2, 3]`| `tup = 1, 2, 3`, `tup = (1, 2, 3)`|
|Empty creation|`li = []`| `tup = ()`|
|Single Element|`li = [1]`| `tup = 1,`, `tup = (1,)`|
|Casting| `li = list(1, 2, 3)`| `tup = tuple(1, 2, 3)`|

## Lists

* [0-print_list_integer.py](./0-print_list_integer.py) contains a function that prints all integers of a list, each on a new line  
**Prototype:**

  ```python
  def print_list_integer(my_list=[]):
  ```

* [1-element_at.py](./1-element_at.py) contains  a function that retrieves an element from a list like in C, returning `None` for indexes that are out of range or negative  
**Prototype:**

  ```python
  def element_at(my_list, idx):
  ```

* [2-replace_in_list.py](./2-replace_in_list.py) contains a function that replaces an element of a list at a specific position (like in C)  
**Prototype:**

  ```python
  def replace_in_list(my_list, idx, element):
  ```

* [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py) contains a function that prints all integers of a list, in reverse order, each on a new line.  
**Prototype:**

  ```python
  def print_reversed_list_integer(my_list=[]):
  ```

* [4-new_in_list.py](./4-new_in_list.py) contains a function that replaces an element in a list at a specific position without modifying the original list (like in C).  
**Prototype:**

  ```python
  def new_in_list(my_list, idx, element):
  ```

* [5-no_c.py](./5-no_c.py) contains a function that removes all characters `c` and `C` from a string without using `str.replace()`  
**Prototype:**

  ```python
  def no_c(my_string):
  ```

* [6-print_matrix_integer.py](./6-print_matrix_integer.py) contains a function that prints a matrix of integers.  
**Prototype:**

  ```python
  def print_matrix_integer(matrix=[[]]):
  ```

  **Example:**

  ```python
  matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]

  print_matrix_integer(matrix)
  print("--")
  print_matrix_integer()
  ```

  to give: (_script execution piped with_ `cat -e`)

  ```bash
  1 2 3$
  4 5 6$
  7 8 9$
  --$
  $
  ```

* [9-max_integer.py](./9-max_integer.py) contains a function that finds and returns the biggest integer of a list without using `max()`, returning `None` for empty lists.  
**Prototype:**

  ```python
  def max_integer(my_list=[]):
  ```

* [10-divisible_by_2.py](./10-divisible_by_2.py) contains a function that finds all multiples of 2 in a list returning a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2.  
**Prototype:**

  ```python
  def divisible_by_2(my_list=[]):
  ```

* [11-delete_at.py](./11-delete_at.py) contains a a function that deletes the item at a specific position in a list without usinf `pop()`. If the index is negative or out of range, nothing changes (returns the same list).  
**Prototype:**

  ```python
  def delete_at(my_list=[], idx=0):
  ```

## Tuples

* [7-add_tuple.py](./7-add_tuple.py) contains a function that adds 2 tuples returning a tuple with 2 integers where the first element is the addition of the first elements of both tuple arguments, similarly for the second element. `0` is used for missing integers i.e. a tuple smaller than 2, and elements after the first two ignored.  
**Prototype:**

  ```python
  def add_tuple(tuple_a=(), tuple_b=()):
  ```

* [8-multiple_returns.py](./8-multiple_returns.py) contains a function that returns a tuple with the length of a string, and its first character or `None` if the string is empty.  
**Prototype:**

  ```python
  def multiple_returns(sentence):
  ```

---

### Multiple assignment

* [12-switch.py](./12-switch.py) switches the values of `a` and `b`

## CPython - Lists

An under the hood look at the implementation of Python in C.  
Lists are implementd by the [`PyListObject`](https://docs.python.org/3.4/c-api/list.html) which is a subtype of `PyObject`, the basic structure for these Python implementations

* [100-print_python_list_info](./100-print_python_list_info.c) contains a C funtion that prints some basic info about Python lists.  
**Prototype:**

  ```c
  void print_python_list_info(PyObject *p);
  ```

  **Compilation:**

  ```bash
  gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
  ```

### Usage & Output

  Create a Python file and import `ctypes` then load the just created shared library using the `CDLL` method:

  ```python
  import ctypes

  lib = ctypes.CDLL('./libPyList.so')
  lib.print_python_list_info.argtypes = [ctypes.py_object]
  ```

  Create a list and call the C funtion on it:

  ```python
  li = ['hello', 'World']
  lib.print_python_list_info(li)
  l = []
  lib.print_python_list_info(l)
  l.append(0)
  lib.print_python_list_info(l)
  ```

  Which gives:

  ```bash
  [*] Size of the Python List = 2
  [*] Allocated = 2
  Element 0: str
  Element 1: str
  [*] Size of the Python List = 0
  [*] Allocated = 0
  [*] Size of the Python List = 1
  [*] Allocated = 4
  Element 0: int
  ```

## Technical Interview Preparation

[13-is_palindrome.c](./13-is_palindrome.c) contains a C function that checks if a singly linked list is a palindrome.  
**Prototype:**

```c
int is_palindrome(listint_t **head);
```

**Returns:**  

* `1` for palindromes (including empty lists)

* `0` non-palindromes
