#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check the code for Holberton School students.
 * @head: begining node
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, cont = 0, k = 0;
	listint_t *tmp, *tmp2, *tmp3;

	tmp2 = *head;
	tmp3 = *head;
	if (*head == NULL)
		return (1);
	for (cont = 0; tmp3; cont++)
		tmp3 = tmp3->next;
	if (cont % 2 != 0)
		k = (cont / 2) + 1;
	else
		k = cont / 2;
	for (; k > 0; k--)
		tmp2 = tmp2->next;
	for (i = 0; i < cont / 2; i++)
	{
		j = i;
		tmp = *head;
		for (; j < (cont / 2) - 1; j++)
			tmp = tmp->next;
		if (tmp->n == tmp2->n)
			tmp2 = tmp2->next;
		else
			return (0);
	}
	return (1);
}
