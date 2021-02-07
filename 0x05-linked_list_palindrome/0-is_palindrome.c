#include "lists.h"

/**
 * is_palindrome - a function in C that checks if a singly linked list is a palindrome.
 * @head: Pointer to the head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;

	int array[1000], i = 0, j = 0, m;

	if (head == NULL || (curr != NULL && curr->next == NULL))
		return (1);
	while (curr != NULL)
	{
		array[i] = curr->n;
		curr = curr->next;
		i++;
	}
	i--, m = i / 2;
	while (i >= m && j <= m)
	{
		if (array[j] != array[i])
			return (0);
		i--, j++;
	}
	return (1);
}