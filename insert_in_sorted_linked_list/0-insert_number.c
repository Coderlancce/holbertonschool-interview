#include "lists.h"

/* This function insert in a sorted linked list a new pointer
*/

listint_t *insert_node(listint_t **head, int number) {
    /*
    new - save the pointer to new number insert
    current -run for all pointers and remember where i'm
    */
    listint_t *new;
	listint_t *current;

    /*start point*/
    current = *head;

    /*reserve memory for the new pointer*/
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    /*assign value*/
    new->n = number;

    /*search the posision and conect the new pointer*/
    while (current && current->next && current->next->n < number)
        current = current->next;

    /*now for reconect the new pointer we need know if have more pointer to conect or if we are in the finish list*/
    if ((current == NULL) || (number < current->n)) {
        new->next = *head;
        *head = new;
    }
    else {
        new->next = current->next;
        current->next = new;
    }

    /*return the new pointer*/
    return new;
}