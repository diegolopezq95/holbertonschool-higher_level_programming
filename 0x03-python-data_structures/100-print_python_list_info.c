#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to an python object
 * Return Nothing
 */

void print_python_list_info(PyObject *p)
{
	unsigned int i;
	PyObject *pitem;

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < Py_SIZE(p); i++)
		{
			pitem = PyList_GetItem(p, i);
			printf("Element %u: %s\n", i, Py_TYPE(pitem)->tp_name);
		}
	}
}
