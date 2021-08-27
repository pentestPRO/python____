#include <stdio.h>
#include <stdlib.h>

struct tree
{
    int data;
    struct tree *left;
    struct tree *right;
};

struct tree *node(int value)
{
    struct tree *p = (struct tree *)malloc(30 * sizeof(struct tree));
    p->data = value;
    p->left = NULL;
    p->right = NULL;
    return p;
}

struct tree *preorder(struct tree *ptr)
{
    if (ptr != NULL)
    {
        printf("THE VALUE IS : %d", ptr->data);
        printf("\n");
        preorder(ptr->left);
        printf("\n");
        preorder(ptr->right);
    }
}

struct tree *postorder(struct tree *ptr)
{
    if (ptr != NULL)
    {
        preorder(ptr->left);
        printf("\n");
        preorder(ptr->right);
        printf("THE VALUE IS : %d", ptr->data);
        printf("\n");
    }
}

struct tree *inorder(struct tree *ptr)
{
    if (ptr != NULL)
    {
        preorder(ptr->left);
        printf("\n");
        printf("THE VALUE IS : %d", ptr->data);
        printf("\n");
        preorder(ptr->right);
    }
}
int main()
{

    struct tree *root = node(50);
    struct tree *first = node(60);
    struct tree *second = node(10);
    struct tree *third = node(50);

    root->left = first;
    root->right = second;
    first->left = third;
    printf("preorder start : \n");
    preorder(root);
    printf("postorder start :\n");
    postorder(root);
    printf("inorder start : \n");
    inorder(root);
    return 0;
}
