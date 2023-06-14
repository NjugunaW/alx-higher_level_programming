#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - function that prints some basic info about Python lists
 * @p: pointer
 */
void print_python_list(PyObject *p)
{
  int ab, distrbt, n;
  const char *type;
  PyListObject *list = (PyListObject *)p;
  PyVarObject *var = (PyVarObject *)p;

  ab = var->ob_size;
  distrbt = list->allocated;

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %d\n", ab);
  printf("[*] Allocated = %d\n", distrbt);

  for (n = 0; n < ab; n++)
    {
      type = list->ob_item[n]->ob_type->tp_name;
      printf("Element %d: %s\n", n, type);
      if (strcmp(type, "bytes") == 0)
	print_python_bytes(list->ob_item[n]);
    }
}

/**
 * print_python_bytes - fnctn that prints basic info about Python byte objects
 * @p: pointer
 */
void print_python_bytes(PyObject *p)
{
  unsigned char ch, ab;
  PyBytesObject *bytes = (PyBytesObject *)p;

  printf("[.] bytes object info\n");
  if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
      printf("  [ERROR] Invalid Bytes Object\n");
      return;
    }

  printf("  ab: %ld\n", ((PyVarObject *)p)->ob_size);
  printf("  trying string: %s\n", bytes->ob_sval);

  if (((PyVarObject *)p)->ob_size > 10)
    ab = 10;
  else
    ab = ((PyVarObject *)p)->ob_size + 1;

  printf("  first %d bytes: ", ab);
  for (ch = 0; ch < ab; ch++)
    {
      printf("%02hhx", bytes->ob_sval[ch]);
      if (ch == (ab - 1))
	printf("\n");
      else
	printf(" ");
    }
}
