# Python - Everything is object

This project contains text files(or Python scripts) with answers to different questions on Python with emphasis on its OOP nature.

## Aliasing and Cloning

Since strings are immutable, Python optimizes resources by making two names that refer to the same string value refer to the same object. This is known as **aliasing**.

* `==` determines equality of two items by value
* `is` checks if two items refer to the same object.

[![str 'is' vs '=='](http://www.openbookproject.net/thinkcs/python/english2e/_images/mult_references1.png)](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)  
from the above, `a == b` and `a is b` both evaluate to `True`.

For lists, and other types, this can be done as:

```python
>>> a = [1, 2, 3]
>>> b = a
# Testing
>>> b is a
True
>>> b[0] = 6
>>> print(a)
[6, 2, 3]
```

### Who?  

[0-answer.txt](./0-answer.txt): What function would you use to print the type of an object?

### Where?  

[1-answer.txt](./1-answer.txt): How do you get the variable identifier (which is the memory address in the CPython implementation)?

### Integers

* [2-answer.txt](./2-answer.txt): In the following code, do `a` and `b` point to the same object? (Yes or No).

  ```python
  >>> a = 89
  >>> b = 10
  ```

* [3-answer.txt](./3-answer.txt): In the following code, do `a` and `b` point to the same object? (Yes or No)

  ```python
  >>> a = 89
  >>> b = 89
  ```

* [4-answer.txt](./4-answer.txt): In the following code, do `a` and `b` point to the same object? (Yes or No)

  ```python
  >>> a = 89
  >>> b = a
  ```

* [5-answer.txt](./5-answer.txt): In the following code, do `a` and `b` point to the same object? (Yes or No)

  ```python
  >>> a = 89
  >>> b = a + 1
  ```

* [16-answer.txt](./16-answer.txt): What does this script print?

  ```python
  def increment(n):
      n += 1

  a = 1
  increment(a)
  print(a)
  ```

* [24-answer.txt](./24-answer.txt): What does this script print?

  ```python
  a = (1)
  b = (1)
  a is b
  ```

### Strings

* [6-answer.txt](./6-answer.txt): What do these 3 lines print?

  ```python
  >>> s1 = "Best School"
  >>> s2 = s1
  >>> print(s1 == s2)
  ```

* [8-answer.txt](./8-answer.txt): What do these 3 lines print?

  ```python
  >>> s1 = "Best School"
  >>> s2 = "Best School"
  >>> print(s1 == s2)
  ```

* [7-answer.txt](./7-answer.txt): What do these 3 lines print?

  ```python
  >>> s1 = "Best"
  >>> s2 = s1
  >>> print(s1 is s2)
  ```

* [9-answer.txt](./9-answer.txt): What do these 3 lines print?

  ```python
  >>> s1 = "Best School"
  >>> s2 = "Best School"
  >>> print(s1 is s2)
  ```

### Lists

* [10-answer.txt](./10-answer.txt): What do these 3 lines print?

  ```python
  >>> l1 = [1, 2, 3]
  >>> l2 = [1, 2, 3] 
  >>> print(l1 == l2) 
  ```

* [11-answer.txt](./11-answer.txt): What do these 3 lines print?

  ```python
  >>> l1 = [1, 2, 3]
  >>> l2 = [1, 2, 3] 
  >>> print(l1 is l2)
  ```

* [12-answer.txt](./12-answer.txt): What do these 3 lines print?

  ```python
  >>> l1 = [1, 2, 3]
  >>> l2 = l1
  >>> print(l1 == l2)
  ```

* [13-answer.txt](./13-answer.txt): What do these 3 lines print?

  ```python
  >>> l1 = [1, 2, 3]
  >>> l2 = l1
  >>> print(l1 is l2)
  ```

* [14-answer.txt](./14-answer.txt): What does this script print?

  ```python
  l1 = [1, 2, 3]
  l2 = l1
  l1.append(4)
  print(l2)
  ```

* [15-answer.txt](./15-answer.txt): What does this script print?

  ```python
  l1 = [1, 2, 3]
  l2 = l1
  l1 = l1 + [4]
  print(l2)
  ```

* [17-answer.txt](./17-answer.txt): What does this script print?

  ```python
  def increment(n):
      n.append(4)

  l = [1, 2, 3]
  increment(l)
  print(l)
  ```

* [18-answer.txt](./18-answer.txt): What does this script print?

  ```python
  def assign_value(n, v):
      n = v

  l1 = [1, 2, 3]
  l2 = [4, 5, 6]
  assign_value(l1, l2)
  print(l1)
  ```

* [19-copy_list.py](./19-copy_list.py): returns a copy of a list.  
**Prototype:**

  ```python
  def copy_list(l):
  ```

* [27-answer.txt](./27-answer.txt): Will the last line of this script print `139926795932424`? (Yes or No)

  ```python
  >>> id(a)
  139926795932424
  >>> a
  [1, 2, 3, 4]
  >>> a = a + [5]
  >>> id(a)
  ```

* [28-answer.txt](./28-answer.txt): Will the last line of this script print `139926795932424`? (Yes or No)

  ```python
  >>> a
  [1, 2, 3]
  >>> id (a)
  139926795932424
  >>> a += [4]
  >>> id(a)
  ```
  
### Tuples

* [20-answer.txt](./20-answer.txt): Is `a` a tuple? (Yes or No)

  ```python
  a = ()
  ```

* [21-answer.txt](./21-answer.txt): Is `a` a tuple? (Yes or No)

  ```python
  a = (1, 2)
  ```
  
* [22-answer.txt](./22-answer.txt): Is `a` a tuple? (Yes or No)

  ```python
  a = (1)
  ```

* [23-answer.txt](./23-answer.txt): Is `a` a tuple? (Yes or No)

  ```python
  a = (1, )
  ```
  
* [25-answer.txt](./25-answer.txt): What does this script print?

  ```python
  a = (1, 2)
  b = (1, 2)
  a is b
  ```

* [26-answer.txt](./26-answer.txt): What does this script print?

  ```python
  a = ()
  b = ()
  a is b
  ```

----

#### [100-magic_string.py](./100-magic_string.py)

Contains a function `magic_string()` that returns a string `"BestSchool"` `n` times the number of the iteration, i.e.

[Calling script](./100-main.py):

```python
for i in range(10):
    print(magic_string())
```

Output:

```bash
$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
```

#### [101-locked_class.py](./101-locked_class.py)

Contains a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name` e.g:

```python
lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

Output:

```bash
[AttributeError] 'LockedClass' object has no attribute 'last_name'
```
