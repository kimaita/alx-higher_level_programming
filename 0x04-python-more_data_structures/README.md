# Python - More Data Structures: Set, Dictionary

## [Set](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset)

A `set` object is an unordered collection of **distinct** hashable objects. Being an unordered collection, sets do not record element position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.  
The set type is **mutable** [^1] — the contents can be changed using methods like `add()` and `remove()`.

**Creation:**

* Use a comma-separated list of elements within braces:  

  ```python
  s = {'jack', 'sjoerd'}
  ```

* Use a set comprehension:  

  ```python
  s = {c for c in 'abracadabra' if c not in 'abc'}
  ```

* Use the type constructor:

  ```python
  s = set() 
  s = set('foobar')
  s = set(['a', 'b', 'foo'])
  ```

**Common Uses:**  

* Membership testing.  
* Eliminating duplicates from a sequence.  
* Mathematical operations like union, intersection, difference, and symmetric difference.

## [Dictionary](https://docs.python.org/3.8/library/stdtypes.html#mapping-types-dict)

A `dictionary` is a mapping object that maps hashable values to arbitrary objects thus creating a 'set' of _key: value_ pairs, with the requirement that the keys are unique (within one dictionary). Dictionaries are indexed by keys, which can be any immutable type(tuples can be used as keys if they contain only strings, numbers, or tuples). Values that are not hashable, that is, values containing lists, dictionaries or other mutable types (that are compared by value rather than by object identity) may not be used as keys.  
Dictionaries are mutable objects.

**Creation:**

* Use a comma-separated list of key: value pairs within braces:  

  ```python
  d = {'jack': 4098, 'sjoerd': 4127}
  ```

* Use a dict comprehension:  

  ```python
  d = {}        
  d1 = {x: x ** 2 for x in range(10)}
  ```

* Use the type constructor:

  ```python
  d = dict()    
  d1 = dict([('foo', 100) ('bar', 200)])
  d2 = dict(foo=100, bar=200)
  ```

**Common Uses:**  

* Storing a value with some key and extracting the value given the key.

### Lambda Functions & `map()`, `reduce()`, `filter()`

 The lambda operator or lambda function is a way to create small _anonymous functions_, i.e. functions without a name. These functions are _throw-away functions_, i.e. they are just needed where they have been created. They are syntactically restricted to a single expression.  
 **Syntax:**

 ```python
 lambda argument_list: expression  
 ```

 The argument list consists of a comma separated list of arguments and the expression is an arithmetic expression using these arguments. You can assign the function to a variable to give it a name.

 **Example:**

 ```python
 #returns the sum of its two arguments
 sum = lambda x, y : x + y
 sum(3,4)       #gives 7
 ```

#### map(): `map(func, seq)`

Applies a function to all elements of a sequence, returning an iterator.  

#### filter(): `filter(func, seq)`

Filters out all elements of a sequence for which a predicate function returns `True`, i.e. the resulting iterator will have those elements for which the function is `True`  

#### reduce(): `reduce(func, seq)`

Continually applies a function to a sequence, returning a single value. (Obtains the result of the function aplied to the first two elements then repeats this with the accumulated value and each subsequent element).  
This function is contained in the `functools` module

[^1]: The `frozenset` is however immutable.
