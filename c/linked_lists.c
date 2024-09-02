#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct list{
    int item;
    struct list *next;
} list_t;

list_t *list_append(list_t *head, int item){
    list_t *temp = head;
    while (temp->next != NULL) temp = temp->next;
    temp->next = (list_t *)malloc(sizeof(list_t));
    temp->next->item = item;
    temp->next->next = NULL;
    return head;
}

list_t * list_remove(list_t *head, int item){
    list_t *temp = head;
    if (temp->item == item) {
        list_t *temp2 = temp->next;
        free(temp);
        return temp2;
    }
    while (temp->next != NULL && temp->next->item != item) temp = temp->next;
    if(temp->next == NULL) return head;
    list_t *temp2 = temp->next;
    temp->next = temp->next->next;
    free(temp2);
    return head;
}

void list_print(list_t *head){
    if(head == NULL) {
        printf("NULL\n");
        return;
    }
    while (head->next != NULL) {
        printf("%i ", head->item);
        head = head->next;
    }
    printf("%i\n", head->item);
}

int main()
{
    list_t *my_list = (list_t *)malloc(sizeof(list_t));
    my_list->item = 0;
    my_list->next = NULL;
    list_append(my_list, 1);
    list_append(my_list, 2);
    list_append(my_list, 3);
    list_append(my_list, 4);
    list_print(my_list);
    my_list = list_remove(my_list, 2);
    list_print(my_list);
    my_list = list_remove(my_list, 99);
    list_print(my_list);
    my_list = list_remove(my_list, 4);
    list_print(my_list);
    my_list = list_remove(my_list, 0);
    list_print(my_list);
    my_list = list_remove(my_list, 3);
    list_print(my_list);
    my_list = list_remove(my_list, 1);
    list_print(my_list);
    return 0;
}
