# Python - Test-driven development

## Interactive Testing

Python's `doctest` module offers a means of performng interactive tests for functions/classes/modules.

The `doctest` module **searches for pieces of text that look like interactive Python sessions**, and then executes those sessions to verify that they work exactly as shown.

### Definition

#### Function tests

These are written as they would be called in an interactive Python session i.e command-line Python, followed by the output as it would appear.

```bash
>>>factorial(5)
120
```

#### Exceptions
  
You only need specify two lines:

1. **Traceback header:**  
  `Traceback (most recent call last):` or `Traceback (innermost last):`
  
2. **Exception type and detail:**  
  Error: message

For instance:

```bash
>>> factorial(-1)
Traceback (most recent call last):
        ...
ValueError: n must be >= 0
```

### Usage

There are several common ways to use `doctest`:

* `testmod()`: checks a module's/function's docstrings.

  [Say a module `example`](https://docs.python.org/3.8/library/doctest.html#simple-usage-checking-examples-in-docstrings):

  ```python
  """
  This is the "example" module.

  The example module supplies one function, factorial().  For example,

  >>> factorial(5)
  120
  """


  def factorial(n):
      """Return the factorial of n, an exact integer >= 0.

      >>> factorial(30)
      265252859812191058636308480000000
      >>> factorial(-1)
      Traceback (most recent call last):
              ...
      ValueError: n must be >= 0
      """

      import math

      if not n >= 0:
          raise ValueError("n must be >= 0")
      if math.floor(n) != n:
          raise ValueError("n must be exact integer")
      if n+1 == n:  # catch a value like 1e300
          raise OverflowError("n too large")
      result = 1
      factor = 2
      while factor <= n:
          result *= factor
          factor += 1
      return result


      if __name__ == "__main__":
          import doctest
          doctest.testmod()
  ```

  Running the script won't display anything unless an example fails, in which case the failing example(s) and the cause(s) of the failure(s) are printed to `stdout`, and the final line of output is `***Test Failed*** N failures.`, where `N` is the number of examples that failed.  
  On running this script with the `-v` switch (for verbose logging)  instead:

  ```bash
  $ python example.py -v
 
  Trying:
    factorial(5)
  Expecting:
    120
  ok
  Trying:
    factorial(30)
  Expecting:
    265252859812191058636308480000000
  ok
  Trying:
    factorial(-1)
  Expecting:
    Traceback (most recent call last):
            ...
    ValueError: n must be >= 0
  ok
  2 items passed all tests:
    1 tests in __main__
    2 tests in __main__.factorial
  3 tests in 2 items.
  3 passed and 0 failed.
  Test passed.
  ```

* `testfile()` testing by verifying that interactive examples from a test file or a test object work as expected.

  [Say a file `example.txt`](https://docs.python.org/3.8/library/doctest.html#simple-usage-checking-examples-in-a-text-file):

  ```
  Tests factorial as defined in example.py

  >>> from example import factorial

  >>> factorial(5)
  120
  ```

  then a script with:

  ```python
  import doctest
  doctest.testfile("example.txt")
  ```

  Running the script would output nothing unless an example fails or the `-v` switch was specified for verbosity.

Command-line shortcuts for running the tests directly, as opposed to including this in the module:

|`testmod()`|`testfile()` |
|---|----|
|`python -m doctest -v example.py`|`python -m doctest -v example.txt`|

(The extension is not `.py` so `testfile()` is inferred)
