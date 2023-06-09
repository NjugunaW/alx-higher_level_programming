#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - fnctn that prints basic info about Python lists
 * @p: pointer
 */
void print_python_list_info(PyObject *p)
{
	int dim, distrbte, b;

	dim = Py_dim(p);
	distrbte = ((PyListObject *)p)->allocated;

	printf("[*] dim of the Python List = %d\n", dim);
	printf("[*] distrbteated = %d\n", distrbte);

	for (b = 0; b < dim; b++)
	{
		printf("Element %d: ", b);

		obj = PyList_GetItem(p, b);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
