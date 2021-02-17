#include "lists.h"

/**
 * check_cycle - Check if a single list is a cycle
 * @list: pointed to the linked list head
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *rabbit;
    
    if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);

	turtle = rabbit = list;
	while (turtle && rabbit && rabbit->next)
	{
		turtle = turtle->next;
		rabbit  = rabbit->next->next;
		if (turtle == rabbit)
			return (1);
		}
	return (0);
}