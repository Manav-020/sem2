#include <iostream>
using namespace std;
#define n 5
class stack{
    public:
        int top=-1;
        int arr[n];
};
class stack s1;
void push(int x)
{
    if(s1.top==n-1)
    {
        cout<<"stack overflow";
    }
    else
    {
        s1.top++;
        s1.arr[s1.top]=x;
    }
}
void pop()
{
    if(s1.top==-1)
    {
        cout<<"stack is empty";
    }
    else
    {
        cout<<"element "<<s1.arr[s1.top]<<" removed from stack";
        s1.top--;
    }
}
void peek()
{
    cout<<"element at top is"<<s1.arr[s1.top];
}
void isFull()
{
    if(s1.top==n-1)
    {
        cout<<"stack is full";
    }
}
void display()
{
    int i=0;
    while (i<=s1.top)
    {
        cout<<s1.arr[i]<<"\t";
        i++;
    }
}
void isEmpty()
{
    if(s1.top==-1)
    {
        cout<<"stack is empty";
    }
}
int main()
{
    int x;
    cout<<"enter element of stack\n";
    for (int i=0;i<n;i++)
    {
        cout<<"enter element:";
        cin>> x;
        push(x);
    }
    pop();
    isFull();
    display();
}
