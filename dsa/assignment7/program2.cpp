#include<bits/stdc++.h>
using namespace std;
class node{
    public:
        int data;
        node *next;
};
void enq(node* &front,node* &rear,int x)
{
    node*n=new node;
    n->data=x;
    if(front==nullptr)
    {
        cout<<x<<" enqueued in the queue"<<endl;
        n->next=nullptr;
        front=rear=n;
    }
    else{
        cout<<x<<" enqueued in the queue"<<endl;
        n->next=nullptr;
        rear->next=n;
        rear=n;
    }
}
void dq(node* &front,node*&rear)
{
    node *temp=new node;
    temp=front;
    if(front==nullptr)
    {
        cout<<"queue is empty"<<endl;
    }
    else if(front==rear)
    {
        delete(front);
        front=rear=nullptr;
    }
    else{
        cout<<front->data<<" removed from the queue"<<endl;
        front=front->next;
        delete(temp);
    }
}
void peek(node* &front)
{
    if(front==nullptr)
    {
        cout<<"queue is empty"<<endl;
    }
    else
    {
        cout<<front->data<<" is at front of queue"<<endl;
    }
}
int isEmpty(node* &front,node*&rear)
{
    if(front==nullptr && rear==nullptr)
    {
        cout<<"queue is empty\n";
        return 1;
    }
    else{
        return 0;
    }
}
void display(node* &front,node*&rear)
{
    node *temp=new node;
    temp=front;
    while(temp!=nullptr)
    {
        cout<<temp->data<<"\t";
        temp=temp->next;
    }
    cout<<endl;
}
int main()
{
    node*front,*rear;
    front=rear=nullptr;
    int c,x;
    enq(front,rear,1);
    enq(front,rear,2);
    enq(front,rear,7);
    enq(front,rear,5);
    while (true)
    {
        cout<<"press 1 to enqueue.\n"<<"press 2 to dequeue.\n"<<"press 3 to peek.\n"<<"press 4 to perfrom isEmpty.\n"<<"press 5 to display.\n"<<"press 6 to exit.\n\n"<<endl;
        cout<<"enter choice:";
        cin>>c;
        switch(c)
        {
            case 1: cout<<"enter element you want to enqueue:";
                cin>>x;
                enq(front,rear,x);
                break;
            case 2:dq(front,rear);
                break;
            case 3:peek(front);
                break;
            case 4:cout<<isEmpty(front,rear);
                break;
            case 5:display(front,rear);
                break;
            case 6: return 0;
        }
        cout<<"\n\n";
    }
}