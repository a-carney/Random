#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct LinkedList {
    struct node *head;
    struct node *tail;
};

#define MAX 10
#define NEW_LINKED_LIST() (struct LinkedList *)malloc(sizeof(struct LinkedList))

int getRandomInt(int min, int max) {
    return (rand() % (max - min + 1)) + min;
}

void bubble_sort(int *arr, int n) {
    int *left, *right, temp;
    for (left = arr; left < (arr + n - 1); left++) {
        for (right = arr; right < (arr + n - (left - arr) - 1); right++) {
            if (*right > *(right + 1)) {
                temp = *right;
                *right = *(right + 1);
                *(right + 1) = temp;
            }
        }
    }
}
              
int main() {

    // create linked list of 10 random numbers
    struct LinkedList *list = LinkedList;
    printf("list: %p\n", list);
    list->head = NULL;
    list->tail = NULL;
    for (int i = 0; i < MAX; i++) {
	struct node *newNode = (struct node *)malloc(sizeof(struct node));
	newNode->data = getRandomInt(1, 100);
	newNode->next = NULL;
	if (list->head == NULL) {
	    list->head = newNode;
	    list->tail = newNode;
	} else {
	    list->tail->next = newNode;
	    list->tail = newNode;
	}
	printf("newNode: %p\n", newNode);
    }
    printf("Sorting Info:\n");
    printf("BEFORE: list: %p\n", list);
    
    bubble_sort(list, MAX);
    printf("AFTER: list: %p\n", list);

    return 0;
}
