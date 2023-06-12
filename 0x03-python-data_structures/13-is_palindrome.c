#include "lists.h"
#include <stddef.h>

/**
 * list_reverse - a function that reverses a singly-linked list
 * @head: pointer to a struct
 * Return: A pointer to the head of the reversed list.
 */
listint_t *list_reverse(listint_t **head)
{
	listint_t *nde = *head, *next, *last = NULL;

	while (nde)
	{
		next = nde->next;
		nde->next = last;
		last = nde;
		nde = next;
	}

	*head = last;
	return (*head);
}

/**
 * is_palindrome - a function that checks if a list is a palindrome
 * @head: pointer to a sturct
 * Return: 0 if linked list not a palindrome
 *         1 if linked list is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *centre;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = list_reverse(&temp);
	centre = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	list_reverse(&centre);

	return (1);
}
