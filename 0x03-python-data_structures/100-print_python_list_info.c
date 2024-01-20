#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int s = PyList_Size(p);
	int i;
	PyListObject *o = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n" o->allocated);
	for (i = 0; i < s; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(O->ob_item[i]->tp_name);
	}
}
