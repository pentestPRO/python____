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

    } while (ptr != NULL);
    
 
    
}

// functions for insertatfirst and deleteatfirst:
struct link * insertatfirst(struct link * head){
    int value;
    printf("ENTER A VALUE TO INSERT IN DOUBLYLINKLIST : ");
    scanf("%d",&value);

    struct link * ptr = (struct link *)malloc(30*sizeof(struct link));
    ptr->data = value;
    ptr->next = head;
    ptr->priv = NULL;
    return ptr;

}

struct link * deleteatfirst(struct link *head){
    struct link * ptr = head;
    head = head->next;
    head->priv = NULL;
    free(ptr);
    return head;
}
//functions for insertatindex and deleteatindex :
struct link * insertatindex(struct link * head){
    int index,value;
    printf("ENTER A INDEX TO INSERT IN DOUBLYLINKLIST : ");
    scanf("%d",&index);
    printf("ENTER A VALUE TO INSERT IN DOUBLYLINKLIST : ");
    scanf("%d",&value);

    struct link * ptr = (struct link *)malloc(30*sizeof(struct link));
    struct link * p = head;
    struct link * q = head->next;
    ptr->data = value;
    for (int i = 0; i < index - 1; i++)
    {
        p = p->next;
        q = q->next;
    }
    p->next = ptr;
    ptr->next = q;
    return head;
    
    
}

struct link * deleteatindex(struct link * head){
    int index;
    printf("ENTER A INDEX TO DELETE A NODE IN DOUBLYLINKLIST : ");
    scanf("%d",&index);

    struct link * p = head;
    struct link * q = head->next;
    
    for (int i = 0; i < index - 1; i++)
    {
        p = p->next;
        q = q->next;
    }
    p->next = q->next;
    free(q);
    return head;

}

//functions for insertatnode and deleteatnode :
struct link * insertatnode(struct link * head){
    int value,node;
    printf("ENTER A VALUE TO INSERT IN DOUBLYLINKLIST : ");
    scanf("%d",&value);
    printf("ENTER A NODE TO WHERE INSERT A VALUE IN DOUBLYLINKLIST : ");
    scanf("%d",&node);
    struct link * ptr = (struct link *)malloc(30*sizeof(struct link));
    struct link * p = head;
    struct link * q = head->next;
    ptr->data = value;
    while (q->data != node)
    {
        p = p->next;
        q = q->next;
    }
    p->next = ptr;
    ptr->next = q;
    return head;
    

}

// functions for insertatlast and deleteatlast :

struct link * insertatlast(struct link * head){
    int value,node;
    printf("ENTER A VALUE TO INSERT IN DOUBLYLINKLIST : ");
    scanf("%d",&value);
    struct link * ptr = (struct link *)malloc(30*sizeof(struct link));
    struct link * p = head;
    
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
   
    struct link * ptr = (struct link *)malloc(30*sizeof(struct link));
    struct link * p = head;
    struct link * q = head->next;

    while (q->next != NULL)
    {
        p = p->next;
        q = q->next;
    }
    p->next = NULL;
    free(q);
    return head;
}
int main(){
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
    fourth->next = NULL;
    fourth->priv = third;
    traversal(head);
    printf("\n");
    //head = insertatfirst(head);
    //head = deleteatfirst(head);
    //head = insertatindex(head);
    //head = deleteatindex(head)
    //head = insertatnode(head);
    //head = insertatlast(head);
    head = deleteatlast(head);
    traversal(head);
  
    return 0;
}