#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - fnctn that inserts a num into a sorted singly linked list
 * @head: pointer to another pointer
 * @number: integer
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *latest;

	latest = malloc(sizeof(listint_t));
	if(latest == NULL)
		return (NULL);
	latest->n = number;

	if(node == NULL || node->n >= number)
	{
		latest->next = node;
		*head = latest;
		return(latest);
	}
	while(node && node->next && node->next->n < number)
		node =node->next;
	latest->next = node->next;
	node->next = latest;
	return (latest);
}
