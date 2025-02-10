//using linked list
#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node*next;
};
struct node*top,*temp;
void push(int x)
{
    struct node*new;
    new=(struct node*)malloc(sizeof(struct node));
    new->data=x;
    if(top==NULL)
    {
        new->next=NULL;
        top=new;
    }
    else
    {
        new->next=top;
        top=new;
    }
}
void display()
{
    printf("stack is:\n");
    temp=top;
    if(top==NULL)
    {
        printf("stack is empty");
    }
    else{
        while(temp!=NULL)
        {
            printf("%d\n",temp->data);
            temp=temp->next;
        }
    printf("\n");
    }
}
void pop()
{
    if(top!=NULL){
        temp=top;
        printf("%d removed from stack\n",top->data);
        top=top->next;
        free(temp); 
    }  
    else{
        printf("stack is empty");
    } 
}
void isEmpty()
{
    if(top=NULL)
    {
        printf("stack is empty");
    }
    else{
        printf("stack is not empty");
    }
}
void peek()
{
    if(top==NULL)
    {
        printf("list is empty");
    }
    else{
        printf("top element is:%d",top->data);
    }
}
int main()
{
    int n,x;
    top=NULL;
    printf("enter number of elements you want to enter:");
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        printf("enter element:");
        scanf("%d",&x);
        push(x);
    }
    int i,c;
    while(i=1)
    {   
        printf("\n\npress\n");
        printf("1.to push\n2.to pop\n3.to peek\n4.to check if empty\n5.to exit\n\n\n");
        printf("enter choice:");
        scanf("%d",&c);
        switch(c)
        {
            case 1:printf("enter element you want to push:");
                    scanf("%d",&x);
                    push(x);
                    display();
                    break;
            case 2:pop();
                    display();
                    break;
            case 3:peek();
                break;
            case 4:isEmpty();
                break;
            case 5: return 0;
        }
    }
}