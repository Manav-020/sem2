#include <bits/stdc++.h>
using namespace std;

class node {
public:
    int data;
    node *next;
};

void enq(node *&front, node *&rear, int x) {
    node *n = new node;
    n->data = x;
    if (front == nullptr && rear == nullptr) {
        front = rear = n;
        n->next = front;
    } else {
        n->next = front;
        rear->next = n;
        rear = n;
    }
}

void dq(node *&front, node *&rear) {
    if (front == nullptr && rear == nullptr) {
        cout << "Queue is empty" << endl;
        return;
    }
    node *t = front;
    if (front == rear) {
        front = rear = nullptr;
    } else {
        front = front->next;
        rear->next = front;
    }
    delete t;
}

void display(node *&front, node *&rear) {
    if (front == nullptr) {
        cout << "Queue is empty" << endl;
        return;
    }
    node *t = front;
    do {
        cout << t->data << "\t";
        t = t->next;
    } while (t != front);
    cout << endl;
}

void peek(node *&front, node *&rear) {
    if (front == nullptr && rear == nullptr) {
        cout << "Queue is empty" << endl;
    } else {
        cout << front->data << " is at front" << endl;
    }
}

void isempty(node *&front, node *&rear) {
    if (front == nullptr && rear == nullptr) {
        cout << "Queue is empty" << endl;
    } else {
        cout << "Queue is not empty" << endl;
    }
}

int main() {
    node *front = nullptr, *rear = nullptr;
    enq(front,rear,1);
    enq(front,rear,2);
    int choice, value;
    do {
        cout << "\nCircular Queue Menu" << endl;
        cout << "1. Enqueue" << endl;
        cout << "2. Dequeue" << endl;
        cout << "3. Display" << endl;
        cout << "4. Peek" << endl;
        cout << "5. Check if Empty" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter value to enqueue: ";
            cin >> value;
            enq(front, rear, value);
            break;
        case 2:
            dq(front, rear);
            break;
        case 3:
            display(front, rear);
            break;
        case 4:
            peek(front, rear);
            break;
        case 5:
            isempty(front, rear);
            break;
        case 6:
            cout << "Exiting..." << endl;
            break;
        default:
            cout << "Invalid choice, please try again." << endl;
        }
    } while (choice != 6);
    
    return 0;
}


