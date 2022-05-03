#include "lists.h"
/**
 * check_cycle - Check linked list for a cycle
 *
 * @list: list
 * Return: 1 if has a cycle 0 if hasn't
 */
int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
		return (0);

	while (list != NULL && list->next != NULL)
	{
		if (list->next >= list)
			break;
		list = list->next;
	}

	if (list->next)
		return (1);

	return (0);
}
