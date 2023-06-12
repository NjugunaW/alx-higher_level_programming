#include <stdio.h>
#include <stdlib.h>
#include "Python.h"

/**
 * print_python_list_info - fnctn that prints basic info about Python lists
 * @p: pointer
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *py_list = NULL;
	size_t length = 0, x = 0;
	const char *py_type = NULL;

	length = PyList_Size(p);
	py_list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));
	for  (; x < length; i++)
	{
		py_type = Py_TYPE(py_list->ob_item[x])->tp_name;
		printf("Element %ld: %s\n", x, py_type);
	}
}
