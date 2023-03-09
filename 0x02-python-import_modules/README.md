# Python - import & modules

## `import`

An introduction to python `import` used to import functions from another file into the current one and the subsequent usage.  
The tasks here require running without executing code[^2] when importing.

* [0-add.py](./0-add.py) imports `add(a, b)` from the file [add-0.py](./add_0.py), sets `a = 1` and `b = 2` and prints the result of the addition  
**Output:**

  ```bash  
  1 + 2 = 3
  ```

* [1-calculation.py](./1-calculation.py) is a program that imports and calls each function from the file [calculator_1.py](./calculator_1.py), sets `a = 10` and `b=5` does the Maths, and prints the result. The code should not execute when importing.  
**Output:**

  ```bash
  10 + 5 = 15
  10 - 5 = 5
  10 * 5 = 50
  10 / 5 = 2
  ```

## Command line arguments

These arguments are stored in the `sys` module’s `argv` attribute as a list[^1].
Accessing these elements:

```python
import sys
sys.argv[index]
```

* [2-args.py](./2-args.py) prints the number of and the list of its arguments each on a line
**Example:**

  ```bash
  $ ./2-args.py 
  0 arguments.

  $ ./2-args.py Hello Welcome To The Best School
  6 arguments:
  1: Hello
  2: Welcome
  3: To
  4: The
  5: Best
  6: School
  ```

* [3-infinite_add.py](./3-infinite_add.py) prints the result of the addition of all arguments. The arguments can be cast to integers.  
**Example:**

  ```bash
  $ ./3-infinite_add.py
  0

  $ ./3-infinite_add.py 79 10 -40 -300 89 
  -162
  ```

* [5-variable_load.py](./5-variable_load.py) imports the variable `a` from [variable_load_5.py](./variable_load_5.py) and prints its value.  
**Output:**

  ```bash
  98
  ```

## [Module](https://docs.python.org/3.8/tutorial/modules.html)
>
> File containing Python definitions and statements

* [4-hidden_discovery.py](./4-hidden_discovery.py) prints all the names defined by a [compiled module](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc) that do not start with __, in alpha order  
**Output:**

  ```bash
  $ ./4-hidden_discovery.py | sort
  my_secret_santa
  print_hidden
  print_school
  ```

[^1]: script name is usually index 0  
[^2]: This can be confirmed by importing using `__import__`  _e.g_ for [0-add](./0-add.py):

    ```bash
    $ cat 0-import_add.py
	__import__("0-add")
	$ python3 0-import_add.py
	$
	```