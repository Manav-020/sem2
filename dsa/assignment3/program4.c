#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node*next;
};
struct node*head,*temp;
void insert(int x)
{
    struct node*new;
    new=(struct node*)malloc(sizeof(struct node));
    new->data=x;
    if(head==NULL)
    {
        head=new;
        new->next=NULL;
        temp=new;
    }
    else
    {
        temp->next=new;
        new->next=NULL;
        temp=new;
    }
}
void print()
{
    struct node*t;
    temp=head;
    while (temp!=NULL)
    {
        t=temp;
        printf("%d\t",temp->data);
        temp=temp->next;
        free(t);
    }
    printf("\n");
}
int main()
{
    head=NULL;
    int b;
    printf("enter number of elemtents you want to enter:");
    scanf("%d",&b);
    int z[b];
    int i=0;
    printf("enter elements of array:\n");
    while(i<b)
    {
        printf("enter element:");
        scanf("%d",&z[i]);
        insert(z[i]);
        i++;
    }
    printf("linked list is:\n");
    print();
}