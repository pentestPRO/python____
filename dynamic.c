
#include<stdio.h>
#include<stdlib.h>

int main()
{
int sum=0;
int *ptr;
int *p;
int n;

ptr = (int *) malloc(1 * sizeof(int));


for(int i=0; i<1;i++)
{
    printf("enter the vlaue that store dynamically of %d: ",i);
    scanf("%d",&ptr[i]);
    
}
for (int i = 0; i < 1; i++)
 {
     printf("the  %d value is:  %d",i,ptr[i]);
     printf("\n");
 }
 free(ptr);
 printf("\n");

 ptr = realloc(ptr,2*sizeof(int));
 for(int i=0; i<2;i++)
{
    printf("enter the vlaue that store dynamically of %d: ",i);
    scanf("%d",&ptr[i]);
    
}
for (int i = 0; i < 2; i++)
 {
     printf("the  %d value is:  %d",i,ptr[i]);
     printf("\n");
 }
 
 for(int j=0;j<2;j++)
 {
     sum = sum + ptr[j];
     
 }
printf(" the sum of all numbers : %d",sum);
printf("\n");

printf("how many memory bites you have :");
scanf("%d",&n);
p = (int *) calloc(n, sizeof(int));
if (p == NULL)
{
    printf("NULL :");
}
else{
 for(int i=0; i<n;i++)
{
    printf("enter the vlaue that store dynamically of %d: ",i);
    scanf("%d",&p[i]);
    
}
for (int i = 0; i < n; i++)
 {
     printf("the  %d value is:  %d",i,p[i]);
     printf("\n");
 }
 
 for(int j=0;j<n;j++)
 {
     sum = sum + ptr[j];
     
 }
 printf("sum of number by calloc is: %d ",sum);
  printf("\n");
}
return 0;
}