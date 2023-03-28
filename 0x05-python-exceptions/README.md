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
