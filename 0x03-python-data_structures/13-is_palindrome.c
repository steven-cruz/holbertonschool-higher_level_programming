#include "lists.h"

/**
 * is pal - function that check values of head and tail in a liked list.
 * @head: double pointer to head of linked list.
 * @tail: single pointer to tail of linked list.
 * Return: 1 if palidrome or 0 if not
 */

int is_pal(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);

	if (is_pal(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is palindrome - function to check if singly linked list is a palidrome.
 * @head: double pointer.
 * Return: 0 if not palidrome, 1 if palidrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
			return (1);
	return(is_pal(head, *head));
}
