#include <Python.h>
#include <stdio.h>

/**
* print_python_list_info - prints python list information 
* @p: list
* Return: Void
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, allocated, index = 0;
	PyObject *element;

	list_size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", allocated);
	while (index < list_size)
	{
		element = PyList_GET_ITEM(p, index);
		printf("Element %ld: %s\n", index, element->ob_type->tp_name);
		index++;
	}
}	
