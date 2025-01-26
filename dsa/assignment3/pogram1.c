#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node*next;
};
struct node*head,*temp;
void insert(int x)
{
    struct node*new;//*temp;
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
    printf("enter number of elemtents you want to enter:");
    head=NULL;
    int n,x;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        printf("enter element:");
        scanf("%d",&x);
        insert(x);
    }
    printf("linked list is:\n");
    print();
}