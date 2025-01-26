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
int main()
{
    int n,x;
    struct node*t;
    printf("enter number of elemtents you want to enter:");
    scanf("%d",&n);
    head=NULL;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        printf("enter element:");
        scanf("%d",&x);
        insert(x);
    }
    printf("array is:\n");
    temp=head;
    int i=0;
    while (temp!=NULL)
    {   
        t=temp;
        arr[i]=temp->data;
        temp=temp->next;
        free(t);
        i++;
    }
    for(int i=0;i<n;i++)
    {
        printf("%d\t",arr[i]);
    }   
}