#include "lists.h"
/**
 * check_cycle - a function that checks if a singly linked list has a cycle
 * @list: list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t * cham = list;
	listint_t *har = list;

	if (!list)
		return(0);
	while (cham && har && har->next)
	{
		cham = cham->next;
		har = har->next->next;
		if(cham == har)
			return(1);
	}
	return(0);
}
