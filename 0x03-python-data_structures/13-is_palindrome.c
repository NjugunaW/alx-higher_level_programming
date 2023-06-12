#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
  * is_palindrome - fnctn that checks if a singly linked list is a palindrome
  * @head: pointer to a struct
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int nde = 0, x = 0, *arr = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (tmp)
	{
		nde++;
		tmp = tmp->next;
	}
	arr = malloc(sizeof(int) * nde);
	tmp = *head;
	while (tmp)
	{
		arr[x++] = tmp->n;
		tmp = tmp->next;
	}
	for (x = 0; x < nde / 2; x++)
	{
		if (arr[x] != arr[nde - 1 - x])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
