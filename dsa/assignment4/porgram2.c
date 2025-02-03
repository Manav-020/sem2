#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node*next;
};
struct node*head,*temp;
void delatbeg();
void insert(int x){
    struct node*new;
    new=(struct node*)malloc(sizeof(struct node));
    new->data=x;
    if(head==NULL)
    {
        new->next=NULL;
        head=temp=new;
    }
    else
    {
        new->next=NULL;
        temp->next=new;
        temp=new;
    }
}
void print()
{
    struct node* t = head;
    while(t != NULL)
    {
        printf("%d\t", t->data);
        t = t->next;
    }
    printf("\n");
}
void delend()
{
    struct node* c;
    struct node* t=head;
    while(t->next!=NULL){
        c=t;
        t=t->next;
    }
    if(t==head)
    {
        head=NULL;
        free(t);
    }
    else{
    c->next=NULL;
    free(t);
    }
}
void delatpos(int n)
{
    if(n == 1)
    {
        delatbeg();
        return;
    }
    
    struct node* p = head;
    struct node* t = head;
    int i = 1;
    
    while(i < n && t != NULL)
    {
        p = t;
        t = t->next;
        i++;
    }
    
    if(t == NULL) 
    {
        printf("Position out of range\n");
        return;
    }
    
    p->next = t->next;
    free(t);
}
void delatbeg()
{
    temp=head;
    head=head->next;
    free(temp);
}
int main()
{
    int n,x;
    printf("enter number of elements you want to insert:");
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        printf("enter element:");
        scanf("%d",&x);
        insert(x);
    }
    int a,count=0;
    struct node*z,*y;
    z=y=head;
    for(int i = 0; i < n - count && z != NULL; i++)
    {
        a = z->data;
        y = z->next;
        for(int j = i + 1; j < n - count && y!= NULL; j++)
            {
                if(y == NULL) break;
                if(a == y->data)
                {
                    if(j == n - count - 1)
                    {
                        delend();
                        count++;
                    }
                    else if(j > 0 && j < n - count - 1)
                    {
                        delatpos(j + 1);
                        count++;
                    }
                }
                y=y->next;
            }
        z = z->next;
}
    printf("final linked list after deletion of duplicate data is:\t");
    print();
}