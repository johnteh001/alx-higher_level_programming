/**
 * is_palindrome - function checks if linked list is palindrome
 * @head: head pointer
 *
 * Return: 1 if palindrome, 0 not palindrome
 */
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *mid, *pre_slow, **second_h;
	int result;

	if (head == NULL)
		return (1);
	fast = (*head);
	slow = (*head);
	mid = NULL;
	pre_slow = (*head);
	second_h = head;
	result = 1;

	if ((*head) != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next; /*get the middle */
			pre_slow = slow;
			slow = slow->next;
		} /* fast will become null when there are even elements */
		if (fast != NULL)
		{
			mid = slow;
			slow = slow->next;
		}
		*(second_h) = slow;
		pre_slow->next = NULL;
		rev_list(second_h);
		result = compare_list(*head, *second_h);
		rev_list(second_h);
		if (mid != NULL)
		{
			pre_slow->next = mid;
			mid->next = *second_h;
		}
		else
			pre_slow->next = *second_h;
	}
	return (result);
}
/**
 * reverse - function reverses a linked list
 * @head: head pointer
 * return: nothing
 */
void rev_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *nex;

	while (current != NULL)
	{
		nex = current->next;
		current->next = prev;
		prev = current;
		current = nex;
	}
	*head = prev;
}
/**
 * comparelists - Function compares two linked lists
 * @head1: head pointer argument one
 * @head2: head pointer argument two
 *
 * Return: 1 success, 0 failure
 */
int compare_list(listint_t *head1, listint_t *head2)
{
	listint_t *tmp1 = head1;
	listint_t *tmp2 = head2;

	while (tmp1 && tmp2)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
			return (0);
	}
	if (tmp1 == NULL && tmp2 == NULL)
		return (1);
	return (0);
}
