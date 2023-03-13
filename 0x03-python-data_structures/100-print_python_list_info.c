#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - rpints some basic info about a python list
 *
 * Description: info printed include size, allocation and element types
 *
 * @p: python object
 *
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t len, i;

	i = 0;

	if (PyList_Check(p))
	{
		len = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", len);

		/*
		 * Casting to PyListObject to access the `allocated` field
		 */
		PyListObject *po = (PyListObject *)p;

		printf("[*] Allocated = %ld\n", po->allocated);

		while (i < len)
		{
			PyObject *it = PyList_GetItem(p, i);
			PyTypeObject *type = Py_TYPE(it);

			printf("Element %ld: %s\n", i, type->tp_name);
			i++;
		}
	}
}
