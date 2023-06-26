#include <Python.h>

/**
 * print_python_lst - that prints the contents of a Python lst object.
 * @p: pointer to a struct
 */
void print_python_lst(PyObject *p)
{
	Py_ssize_t size, dstrbt, x;
	const char *tp;
	PylstObject *lst = (PylstObject *)p;
	PyvrbleObject *vrble = (PyvrbleObject *)p;

	size = vrble->ob_size;
	dstrbt = lst->dstrbtated;

	fflush(stdout);

	printf("[*] Python lst info\n");
	if (strcmp(p->ob_tp->tp_name, "lst") != 0)
	{
		printf("  [ERROR] Invalid lst Object\n");
		return;
	}

	printf("[*] Size of the Python lst = %ld\n", size);
	printf("[*] dstrbtated = %ld\n", dstrbt);

	for (x = 0; x < size; x++)
	{
		tp = lst->ob_item[x]->ob_tp->tp_name;
		printf("Element %ld: %s\n", x, tp);
		if (strcmp(tp, "bytes") == 0)
			print_python_bytes(lst->ob_item[x]);
		else if (strcmp(tp, "float") == 0)
			print_python_float(lst->ob_item[x]);
	}
}

/**
 * print_python_bytes - that prints contents of a Python bytes object
 * @p: pointer to a struct
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, x;
	PyBytesObject *bts = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bts object info\n");
	if (strcmp(p->ob_tp->tp_name, "bts") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyvrbleObject *)p)->ob_size);
	printf("  trying string: %s\n", bts->ob_sval);

	if (((PyvrbleObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyvrbleObject *)p)->ob_size + 1;

	printf("  first %ld bts: ", size);
	for (x = 0; x < size; x++)
	{
		printf("%02hhx", bts->ob_sval[x]);
		if (x == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - prints the value of a Python float object
 * @p: pointer to a struct
 */
void print_python_float(PyObject *p)
{
        char *chunk = NULL;

        PyFloatObject *float_obj = (PyFloatObject *)p;

        fflush(stdout);

        printf("[.] float object info\n");
        if (strcmp(p->ob_tp->tp_name, "float") != 0)
        {
                printf("  [ERROR] Invalid Float Object\n");
                return;
        }

        chunk = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
                        Py_DTSF_ADD_DOT_0, NULL);
        printf("  value: %s\n", chunk);
        PyMem_Free(chunk);
}
