#include <stdio.h>
#include <stdlib.h>

struct link
{
    int data;
    struct link *next;
};
int traversal(struct link * ptr){
    
    while (ptr != NULL)
    {
        printf("The value : %d \n",ptr->data);
        ptr = ptr->next;
    }
}
// functions for delete at first and insert at first:
struct link *insertatstart(struct link * head){
    int user;
    printf("PLEASE ENTER A VALID NUMBER : ");
    scanf("%d",&user);
    struct link * ptr = (struct link *)malloc(30 * sizeof(struct link));
    ptr->data = user;

    ptr->next = head;
    return ptr;
}  

struct link *deleteatfirst(struct link * head){
    
    struct link * ptr = head;
    head = head->next;
    free(ptr);
    return head;
}    
// functions for insertatindex and delete a note after index:

struct link * insertatindex(struct link * head){
    int user;
    int index;
    printf("PLEASE ENTER A VALID NUMBER : ");
    scanf("%d",&user);
    printf("PLEASE ENTER A VALID INDEX : ");
    scanf("%d",&index);
    struct link * ptr = (struct link *)malloc(30*sizeof(struct link ));
    struct link *p = head;
    struct link *q = head->next;
    ptr->data = user;

    for (int i = 0; i < index - 1; i++)
    {
        p = p->next;
        q = q->next;
    }
    ptr->next = q;
    p->next = ptr;
    return head;
    
}
struct link * deleteatindex(struct link * head){
    int index;
    printf("PLEASE ENTER A VALID INDEX FOR DELETEING A NODE : ");
    scanf("%d",&index);
    struct link *p = head;
    struct link *q = head->next;
    
    for (int i = 0; i < index - 1; i++)
    {
        p = p->next;
        q = q->next;
    }
    p->next = q->next;
    free(q);
    return head;
    
}

// functions for insertatnode and delete at node:

struct link *insertatnode(struct link *head){
    int value;
    int node;
    printf("PLEASE ENTER A VALID NUMBER : ");
    scanf("%d",&value);
    printf("PLEASE ENTER A VALID NODE : ");
    scanf("%d",&node);
    struct link * ptr = (struct link *)malloc(30 * sizeof(struct link) );
    struct link *p = head;
    struct link *q = head->next;
    ptr->data = value;

    while (q->data != node)
    {
        p = p->next;
        q = q->next;
    }
    ptr->next = q;
    p->next = ptr;
    return head;
    

}

struct link *deleteatnode(struct link * head){
    int node;
    printf("PLEASE ENTER A VALID NODE : ");
    scanf("%d",&node);
    struct link * p = head;
    struct link * q = head->next;
    while (q->data != node)
    {
        p = p->next;
        q = q->next;
    }
    p->next = q->next;
    free(q);
    return head;
    
}

//functions for insertatlast and deleteatlast:

struct link * insertatlast(struct link * head){
    int value;
    printf("PLEASE ENTER A VALID NUMBER : ");
    scanf("%d",&value);
    struct link *ptr = (struct link *)malloc(30 * sizeof(struct link));
    struct link *p = head;
    ptr->data = value;
    while (p->next != NULL)
    {
        p = p->next;
    }
    p->next = ptr;
    ptr->next = NULL;
    return head;
    
}
struct link * deleteatlast(struct link * head){
    struct link * p = head;
    struct link *q = head->next;

    while (q->next != NULL)
    {
        p = p->next;
        q = q->next;
    }
    p->next = NULL;
    free(q);
    return head;
    
}

int main()
{
    struct link *head = (struct link *)malloc(30 * sizeof(struct link));
    struct link *first = (struct link *)malloc(30 * sizeof(struct link));
    struct link *second = (struct link *)malloc(30 * sizeof(struct link));
    struct link *third = (struct link *)malloc(30 * sizeof(struct link));
    head->data = 40;
    head->next = first;
    first->data = 50;
    first->next = second;
    second->data = 60;
    second->next = third;
    third->data = 70;
    third->next = NULL;
    traversal(head);
    printf("\n");

    printf("1) insertatstart");printf("\n");
    printf("2) deleteatfirst");printf("\n");
    printf("3) insertatnode");printf("\n");
    printf("4) deleteatnode");printf("\n");
    printf("5) insertatindex"); printf("\n");
    printf("6) deleteatindex");printf("\n");
    printf("7) insertatlast");printf("\n");
    printf("8) deleteatlast"); printf("\n"); 
    int p = 1;
    int q = 2; 
    
    while (p = q)
    {
       
    int user_num;
    printf("PLEASE CHOOSE A VALID NUMBER : ");
    scanf("%d",&user_num);
    
    

    if (user_num == 1){
        head = insertatstart(head);
        traversal(head);
    }
    else if (user_num == 2){
        head = deleteatfirst(head);
        traversal(head);
    }
    else if (user_num == 3){
        head = insertatnode(head);
        traversal(head);
    }
    else if (user_num == 4){
        head = deleteatnode(head);
        traversal(head);
    }
    else if (user_num == 5){
        head = insertatindex(head);
        traversal(head);
    }
    else if (user_num == 6){
        head = deleteatindex(head);
        traversal(head);
    }
    else if (user_num == 7){
        head = insertatlast(head);
        traversal(head);
    }
    else if (user_num == 8){
        head = deleteatlast(head);
        traversal(head);
    }
    else if (user_num == -1)
    {
        exit(0);
    }

    else{
        exit(0);
        printf("CHOOSE A VALID NUMBER ");
    }
   
    
    }
    
return 0;
}
