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
	ssize_t buf[10000];
	size_t i, j;
	listint_t *tmp = NULL;

	tmp = *head;
	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	i = 0;
	while (tmp != NULL)
	{
		buf[i] = tmp->n;
		tmp = tmp ->next;
		i++;
	}
	j = 0;
	i = i - 1;
	while (i > j)
	{
		if (buf[i++] != buf[j--])
			return (0);
	}
	return (1);
}
