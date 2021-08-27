#include<stdio.h>
#include<stdlib.h>
struct link {
    int data;
    struct link *next;
    struct link *priv;
};

int traversal(struct link * head){
    struct link * ptr = head;
   
    
    do
    {
       
        printf("THE VALUE IS : %d \n",ptr->data);
        ptr = ptr->next;

    } while (ptr != head);
    
}
struct link *insertatfirst(struct link * head,int value){
    struct link * ptr = (struct link *)malloc(30*sizeof(struct link));
    struct link * p = head;
    ptr->data = value;
    while (p->next != head)
    {
        p = p->next;
    }
    p->next = ptr;
    ptr->next  = head;
    head = ptr;
    return ptr;
    
}
int main()
{
    struct link *head = (struct link *)malloc(30 * sizeof(struct link));
    struct link *first = (struct link *)malloc(30 * sizeof(struct link));
    struct link *second = (struct link *)malloc(30 * sizeof(struct link));
    struct link *third = (struct link *)malloc(30 * sizeof(struct link));
    struct link *fourth = (struct link *)malloc(30 * sizeof(struct link));

    head->data = 100;
    head->next = first;
    head->priv = NULL;

    first->data = 200;
    first->next = second;
    first->priv = head;

    second->data = 300;
    second->next = third;
    second->priv = first;

    third->data = 400;
    third->next = fourth;
    third->priv = second;

    fourth->data = 500;
    fourth->next = head;
    fourth->priv = third;
  
  
    traversal(head);
    printf("\n");
  head = insertatfirst(head,10);
  traversal(head);
    return 0;
}