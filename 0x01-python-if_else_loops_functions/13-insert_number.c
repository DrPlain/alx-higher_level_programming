#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Function that inserts a node in sorted list
 * @head: Address of head
 * @number: Number to be inserted
 * Return: Head of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new;
	listint_t *nextPtr;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if ((temp == NULL) || (number < temp->n))
	{
		new->n = number;
		new->next = temp;
		temp = new;
		return (temp);
	}
	else
	{
		while (temp->next)
		{
			nextPtr = temp->next;
			if (number > temp->n && number < nextPtr->n)
			{
				new->n = number;
				new->next = temp->next;
				temp->next = new;
			}
			temp = temp->next;
		}
	}
	return (*head);
}
