#include "lists.h"

/**
 *insert_node - inserts a node at the appropriate position in a linked list
 *@head: Pointer to the head of the linked list 
 *@n: number to be inserted in the new node
 *Return: Pointer to the newly inserted node
*/

listint_t *insert_node(listint_t **head, int n)
{
	listint_t *current_node, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = NULL;

	current_node = *head;

	while (current_node && current_node->next && current_node->next->n <= n)
		current_node = current_node->next;

	if (current_node == NULL)
		*head = new_node;
	else if (current_node->n > n)
	{
		new_node->next = current_node;
		*head = new_node;
	}
	else
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
		}

	return (new_node);
}
