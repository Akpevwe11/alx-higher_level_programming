#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: pointer to list
 *
 * Return: 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp_node = *head;
	int list_length, *element_arr, i;

	if (head == NULL)
		return (1);

	for (list_length = 0; temp_node; list_length++)
		temp_node = temp_node->next;

	element_arr = malloc(sizeof(int) * list_length);
	if (!element_arr)
		exit(100);

	temp_node = *head;
	for (i = 0; temp_node; temp_node = temp_node->next, i++)
		element_arr[i] = temp_node->n;

	for (i = 0; i < (list_length / 2); i++)
	{
		if (element_arr[i] != element_arr[list_length - 1 - i])
		{
			free(element_arr);
			return (0);
		}
	}

	free(element_arr);
	return (1);
}
