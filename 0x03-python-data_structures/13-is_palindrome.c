#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: pointer to list
 *
 * Return: 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev_ptr = NULL;
	listint_t *temp;

	if (head == NULL)
		return (1);

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		temp = slow_ptr->next;
		slow_ptr->next = prev_ptr;
		prev_ptr = slow_ptr;
		slow_ptr = temp;
	}

	if (fast_ptr != NULL)
		slow_ptr = slow_ptr->next;

	while (prev_ptr != NULL && slow_ptr != NULL)
	{
		if (prev_ptr->n != slow_ptr->n)
			return (0);
		prev_ptr = prev_ptr->next;
		slow_ptr = slow_ptr->next;
	}

	return (1);
}

