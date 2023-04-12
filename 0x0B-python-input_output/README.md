# Python - Input/Output

Opening files in Python is pretty easy and straighforward. Use the `open()` function, passing in the filename, and optionally, the open mode and encoding(keyword argument). This returns a file object.

```python
open(filename, mode, encoding=None)
```

The opening mode can be:
|mode|symbol|
|--|----|
|read only|r|rb
|write only|w|wb
|append only| a|ab
|exclusive creation|x

These can be combined with `t` for text files(the default), `b` for binary files and `+` for updating(read/write).  
If the mode is not specified, the function defaults to read. The encoding is platform-dependent if not specified.

This would look like:

```python
opened_file = open('file.txt', 'r' encoding='UTF-8')
```

the opened file is then closed with `f.close()` to free up the file and resources, like so:

```python
opened_file.close()
```

Using a context anager handles the closing and is preferred:

```python
with open('file.txt', 'r' encoding='UTF-8') as opened_file:
    ...
# anything outside the with cannot access the file
```

## Methods

`f` can be taken to be file object returned by a call to `open()`

* The `f.read(size=-1)` method reads in data from the file. Optionally, pass in the number of characters(text mode) or bytes(binary mode) to read, otherwise the entire file contents are read in. This returns a string

* The `f.readline()` method reads a single line from the file, returning the line as a string with the newline character left at the end.

* The `f.readlines()` method or `list(f)` reads in all the lines of a file.
A for-loop can also be used for this purpose like:

  ```python
  for line in f:
      print(line, end='')
  ```

* The `f.write(string)` method writes the contents of `string` to the file, returning the number of characters written. The argument has to be a `str`, or bytes object if in binary mode, so convert any other data type.

* The `f.tell()` method returns an integer giving the file object’s current position in the file represented as number of *bytes* from the beginning of the file.

* The `f.seek(offset, whence)` method can be used to change the file object's position(kind of like moving a cursor) by a given number of bytes. The reference point is determined by `whence` where a value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. `whence` can be omitted and defaults to 0.
