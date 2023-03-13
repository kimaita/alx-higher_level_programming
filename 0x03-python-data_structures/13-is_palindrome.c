#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a songly linked list as a palindrome
 *
 * @head: pointer to linked list head node
 *
 * Return: 0 if no a paindrome
 *	   1 if a palindrome(including empty lists)
 */
int is_palindrome(listint_t **head)
{
	listint_t *it = *head;
	int *elem;
	int i, len, half_len;

	if (it == NULL || list_length(head) == 1)
		return (1);
	i = 0;
	len = list_length(head);
	half_len = len / 2;

	elem = malloc(sizeof(int) * half_len);
	if (elem == NULL)
		exit(98);

	while (i < half_len)
	{
		*(elem + i) = it->n;
		it = it->next;
		i++;
	}

	i--;
	if (len % 2)
		it = it->next;

	while (it)
	{
		printf("%d  ", it->n);
		printf("%d vs %d - ", it->n, *(elem + i));
		if (it->n != *(elem + i))
			return (0);
		i--;
		it = it->next;
	}

	return (1);
}

/**
 * list_length - gets the length of a linked list
 *
 * @head: pointer to linked list head
 *
 * Return: length of linked list
 */
int list_length(listint_t **head)
{
	listint_t *current = *head;
	int i = 0;

	while (current)
	{
		i++;
		current = current->next;
	}
	return (i);
}
