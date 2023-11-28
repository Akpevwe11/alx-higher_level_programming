#include "lists.h"

/**
* check_cycle - check  the likend list have cycle
* @list: head of linked list
*
* Return: 0 if no cycle , 1 if have
*/

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);


		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
