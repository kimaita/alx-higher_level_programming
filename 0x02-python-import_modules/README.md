# Python - import & modules

## `import`

An introduction to python `import` used to import functions from another file into the current one and the subsequent usage

* [0-add.py](./0-add.py) imports `add(a, b)` from the file [add-0.py](./add_0.py), sets `a = 1` and `b = 2` and prints the result of the addition without executing code[^2] when importing  
**Output:**

  ```bash  
  1 + 2 = 3
  ```

* [1-calculation.py](./1-calculation.py) is a program that imports and calls each function from the file [calculator_1.py](./calculator_1.py), sets `a = 10` and `b=5` does the Maths, and prints the result. The code should not execute[^2] when importing.  
**Output:**

  ```bash
  10 + 5 = 15
  10 - 5 = 5
  10 * 5 = 50
  10 / 5 = 2
  ```

## [Module](https://docs.python.org/3.8/tutorial/modules.html)
>
> File containing Python definitions and statements

## Command line arguments

These arguments are stored in the `sys` module’s `argv` attribute as a list[^1].
Accessing these elements:

```python
import sys
sys.argv[index]
```

[^1]: script name is usually index 0  
[^2]: This can be confirmed by importing using `__import__`  _e.g_ for 0-add
```bash
  $ cat 0-import_add.py
  __import__("0-add")
  $ python3 0-import_add.py 
  $ 
```
