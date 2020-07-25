#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_nodeint_at_index - adds a new node at a given position in a list
 * @head: pointer
 * @number: element to add to list
 *
 * Return: address of new node, or NULL if function fails
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *cur;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	cur = *head;
	if (cur == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		while (cur->next != NULL && cur->next->n < number)
			cur = cur->next;
		if (cur->n > number)
		{
			*head = new;
			new->next = cur;
		}
		else
		{
			new->next = cur->next;
			cur->next = new;
		}
	}
	return (new);
}