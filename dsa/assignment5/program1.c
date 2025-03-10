#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node* next;
};
struct node* head,*tail;
void insatbeg(int x)
{
    struct node* new;
    new=(struct node*)malloc(sizeof(struct node));
    if(head!=NULL)
    {
        new->next=head;
        new->data=x;
        tail->next=new;
        head=new;
    }
    else{
        tail=head=new;
        tail->next=new;
        new->data=x;
    }
}
void insatend(int x)
{
    struct node* new;
    new=(struct node*)malloc(sizeof(struct node));
    if(tail!=NULL)
    {
        new->data=x;
        tail->next=new;
        new->next=head;
        tail=new;
    }
    else
    {
        tail=head=new;
        tail->next=new;
        new->data=x;
    }
}
void print()
{
    struct node*temp;
    temp=tail->next;
    while (temp!=tail)
    {
        printf("%d\t",temp->data);
        temp=temp->next;
    }
    if(temp==tail)
    {
        printf("%d",temp->data);
    }
    printf("\n");
}
void insatpos(int pos,int x)
{
    struct node*temp,*new;
    new=(struct node*)malloc(sizeof(struct node*));
    temp=head;
    int i=1;
    while (i<pos-1)
    {
        temp=temp->next;
        i++;
    }
    new->data=x;
    new->next=temp->next;
    temp->next=new;
}
void delatbeg()
{
    struct node*temp;
    temp=head;
    head=head->next;
    tail->next=temp->next;
    free(temp);
}
void delatend()
{
    struct node*temp;
    temp=tail->next;
    while (temp->next!=tail)
    {
        temp=temp->next;
    }
    temp->next=head;
    free(tail);
    tail=temp;
}
int delatpos(int pos)
{
    if(head==NULL){
        printf("list is empty");
        return 0;
    }
    int i=1;
    struct node*temp,*t;
    temp=head;
    while (i<pos)
    {
        t=temp;
        temp=temp->next;
        i++;
    }
    t->next=temp->next;
    free(temp);
}

int main()
{
    int n,i=0,x,c,pos;
    head=tail=NULL;
    printf("enter number of elements you want to enter:");
    scanf("%d",&n);
    while (i<n)
    {
        printf("enter element:");
        scanf("%d",&x);
        insatend(x);
        i+=1;
    }
    while (i=1)
    {
        printf("\n1.Insert an element at a specific position specified by the user.\n2.Insert an element at the beginning of the list\n3.Insert an element at the end of the list.\n4.Delete an element from a specific position specified by the user.\n5.Delete the first element from the list.\n6.Delete the last element from the list.\n7.press 0 to exit\n\n\n");
        printf("enter choice:");
        scanf("%d",&c);
        switch(c)
        {
            case 1:printf("enter position at which you want to enter:");
                    scanf("%d",&pos);
                    printf("enter element:");
                    scanf("%d",&x);
                    insatpos(pos,x);
                    print();
                    break;
            case 2: printf("enter element you want to insert at beginning:");
                    scanf("%d",&x);
                    insatbeg(x);
                    print();
                    break;
            case 3:printf("enter element you want to insert at end:");
                    scanf("%d",&x);
                    insatend(x);
                    print();
                    break;
            case 4:printf("enter position at which you want to delete:");
                    scanf("%d",&pos);
                    delatpos(pos);
                    print();
                    break;
            case 5:delatbeg();
                    print();
                    break;
            case 6:delatend();
                    print();
                    break;
            case 0: return 0;                            
        }
    }
}
