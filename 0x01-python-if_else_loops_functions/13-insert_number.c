#include "lists.h"
/**
 * insert_node - insert node in new position
 * @head: head of the list
 * @number: contain the node
 * Return: new node
 */

listint_t *insert_node(listint_t **head, int number)

{

	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

		if (*head == NULL)
			*head = new;

	else
	{
		if (current->n >= number)
		{
			*head = new;
			new->next = current;
		}
	else
		{
	while ((current->next != NULL) && (current->next->n <= number))
		current = current->next;

				new->next = current->next;
				current->next = new;
		}
	}
	return (new);
}
