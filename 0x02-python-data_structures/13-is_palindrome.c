#include "lists.h"
/**
 * is_palindrome - checks singly linked list is a palindrome
 * @head: begining of linked list
 * Return: 1 if a palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	char array[4000];
	listint_t *walker = *head;
	unsigned int x = 0;
	unsigned int z = 0;

	if (*head == NULL)
		return (1);
	while (walker != NULL)
	{
		array[x] = walker->n;
		walker = walker->next;
		x++;
	}
	x--;
	for (; z < x; x--, z++)
	{
		if (array[z] != array[x])
			return (0);
	}
	return (1);
}
