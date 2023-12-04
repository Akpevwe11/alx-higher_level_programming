#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: pointer to list
 *
 * Return: 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current_node = *head;
	int list_length, *element_array, i;

	if (head == NULL)
		return (1);

	for (list_length = 0; current_node; list_length++)
		current_node = current_node->next;

	element_array = malloc(sizeof(int) * list_length);
	if (!element_array)
		exit(100);

	current_node = *head;
	for (i = 0; current_node; current_node = current_node->next, i++)
		element_array[i] = current_node->n;

	for (i = 0; i < (list_length / 2); i++)
	{
		if (element_array[i] != element_array[list_length - 1 - i])
		{
			free(element_array);
			return (0);
		}
	}

	free(element_array);
	return (1);
}
