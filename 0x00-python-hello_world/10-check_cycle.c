#include "lists.h"

/**
* check_cycle - check  the likend list have cycle
* @list: head of linked list
*
* Return: 0 if no cycle , 1 if have
*/

int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	if (!list || !list->next)
		return (0);

	slow_ptr = list->next;
	fast_ptr = list->next->next;

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		if (slow_ptr == fast_ptr)
			return (1);


		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}
	return (0);
}
