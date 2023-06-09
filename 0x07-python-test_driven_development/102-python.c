#include "Python.h"

/**
 * print_python_string - Prints Python strings.
 * @p: pointer to a struct
 */
void print_python_string(PyObject *p)
{
	long int str_len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	str_len = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", str_len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &str_len));
}
