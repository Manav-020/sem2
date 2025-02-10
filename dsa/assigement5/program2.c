#include <iostream>
using namespace std;
#define n 10

class stack {
public:
    int top = -1;
    int arr[n];
};

stack s1;

void push(int x) {
    if (s1.top == n - 1) {
        cout << "Stack overflow\n";
    } else {
        s1.top++;
        s1.arr[s1.top] = x;
        cout << "Element " << x << " pushed onto stack.\n";
    }
}

void pop() {
    if (s1.top == -1) {
        cout << "Stack is empty\n";
    } else {
        cout << "Element " << s1.arr[s1.top] << " removed from stack\n";
        s1.top--;
    }
}

void peek() {
    if (s1.top == -1) {
        cout << "Stack is empty\n";
    } else {
        cout << "Element at top is " << s1.arr[s1.top] << "\n";
    }
}

void isFull() {
    if (s1.top == n - 1) {
        cout << "Stack is full\n";
    } else {
        cout << "Stack is not full\n";
    }
}

void isEmpty() {
    if (s1.top == -1) {
        cout << "Stack is empty\n";
    } else {
        cout << "Stack is not empty\n";
    }
}

void display() {
    if (s1.top == -1) {
        cout << "Stack is empty\n";
    } else {
        cout << "Stack elements: ";
        for (int i = 0; i <= s1.top; i++) {
            cout << s1.arr[i] << " \t";
        }
        cout << "\n";
    }
}

int main() {
    int choice, x;
    int c;
    cout<<"enter number of elements you want to enter:";
    cin>>c;
    for(int i=0;i<c;i++)
    {
        cout<<"enter element:";
        cin>>x;
        push(x);
    }
    while (true) {
        cout << "\nMenu:\n";
        cout << "1. Push\n";
        cout << "2. Pop\n";
        cout << "3. Peek\n";
        cout << "4. Check if Full\n";
        cout << "5. Check if Empty\n";
        cout << "6. Display\n";
        cout << "7. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter element to push: ";
                cin >> x;
                push(x);
                break;
            case 2:
                pop();
                break;
            case 3:
                peek();
                break;
            case 4:
                isFull();
                break;
            case 5:
                isEmpty();
                break;
            case 6:
                display();
                break;
            case 7:
                cout << "Exiting program.\n";
                return 0;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    }
}
