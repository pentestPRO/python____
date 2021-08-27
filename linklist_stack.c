#include<stdio.h>
#include<stdlib.h>

struct node {
    int data;
    struct node * next;
};
int traversal(struct node *ptr){
    
    while (ptr != NULL)
    {
        printf("The value : %d \n",ptr->data);
        ptr = ptr->next;
    }
}

int Empty(struct node *p){
    if (p == NULL){
        return 0;
    }
    else{
        return 1;
    }
}
int Full(struct node *p){
    struct node *ptr = (struct node *)malloc(30*sizeof(struct node ));
    if (ptr->next == NULL){
        return 0;
    }
    else{
        return 1;
    }
}

struct node *push(struct node * head,int value){
    struct node *ptr = (struct node *)malloc(30*sizeof(struct node ));
    ptr->data = value;
    ptr->next = head;
    head = ptr;
    return ptr;
}

int pop(struct node** ptr){
    struct node *p = *ptr;
    (*ptr) = (*ptr)->next;
    int x = p->data;
    free(p);
    printf("THE VALUE POPED :%d",x);
    printf("\n");
}

int main(){
    struct node *head = NULL;
    head = push(head,60);
    head = push(head,100);
    head = push(head,200);
    traversal(head);
    pop(&head);
    traversal(head);
    printf("%d",Full(head));
    printf("%d",Empty(head));
    return 0;

}