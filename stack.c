#include<stdio.h>
#include<stdlib.h>

struct stack {
 int top ;
 int *arry;
 int size;



};

int traversal(struct stack * ptr){
    int sum = 0;
    while (ptr->top != -1)
    {
        printf("THE DATA AT %d IS : %d",ptr->top,ptr->arry[ptr->top]);
        sum = sum + ptr->arry[ptr->top];
        ptr->top--;
        printf("\n");
    }
    printf(" THE SUM OF ALL DATA :%d",sum);
    printf("\n");
  
    
}
int peek(struct stack * ptr,int i){
    int val = ptr->top -i + 1;
    if (i < 0 ){
        printf("GIVEN INDEX IS NOT AVAILABLE");
        printf("\n");
    }
    else{
        printf("THE VALUE AT  INDEX %d IS : %d",i,ptr->arry[val]);
        printf("\n");
    }
}


int empty(struct stack * ptr){
    if (ptr->top == -1){
        return 0;
    }
    else{
        return 1;
    }

}
int full(struct stack * ptr){
    if (ptr->top == ptr->size - 1){
        return 0;
    }
    else{
        return 1;
    }
}
struct stack *push_stack(struct stack * ptr,int value){
    ptr->top ++;
    ptr->arry[ptr->top] = value;
}

int pop_stack(struct stack * ptr){
    int val = ptr->arry[ptr->top];
    ptr->top--;
    return val;
   
}

int main(){
    struct stack * ptr = (struct stack *)malloc(30*sizeof(struct stack));
    ptr->size = 50;
    ptr->top = -1;
    ptr->arry  = (int *)malloc(ptr->size * sizeof(int));

    printf("%d",empty(ptr));
    printf("%d",full(ptr));
    printf("\n");
    push_stack(ptr,22);
    push_stack(ptr,20);
    push_stack(ptr,21);
    push_stack(ptr,25);
    printf("%d",empty(ptr));
    printf("%d",full(ptr));
    printf("\n");
    printf(" POP VALUE IS : %d",pop_stack(ptr));
    printf("\n");
    peek(ptr,3);
    printf("\n");
    traversal(ptr);
    
    

return 0;

}