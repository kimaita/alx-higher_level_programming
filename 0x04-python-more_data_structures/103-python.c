#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes - prints info about a PyBytesObject
 * @p: a PyObject
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_Size(p);
		const char *data;

		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", PyBytes_AsString(p));

		PyBytes_AsStringAndSize(p, (char **)&data, &size);

		size = ((size + 1) <= 10) ? size + 1 : 10;
		printf("  first %ld bytes:", size);
		for (int i = 0; i < size; i++)
			printf(" %02x", (unsigned char)data[i]);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_list - prints some basic info about a PyListObject
 * @p: a PyObject
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t len, i;
		PyListObject *po = (PyListObject *)p;

		i = 0;
		len = PyList_Size(p);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", len);
		printf("[*] Allocated = %ld\n", po->allocated);

		while (i < len)
		{
			PyObject *it = PyList_GET_ITEM(po, i);

			printf("Element %ld: %s\n", i, it->ob_type->tp_name);
			if (PyBytes_Check(it))
				print_python_bytes(it);
			i++;
		}
	}
}
