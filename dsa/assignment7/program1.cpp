
#include<bits/stdc++.h>
using namespace std;

int evaluate(const string &expression) {
    stack<int> s;
    
    for (char ch : expression) {
        if (isdigit(ch)) {
            s.push(ch - '0');
        } else {
            int val2 = s.top();
            s.pop();
            int val1 = s.top();
            s.pop();
            
            switch (ch) {
                case '+': s.push(val1 + val2); 
                        break;
                case '-': s.push(val1 - val2);  
                        break;
                case '*': s.push(val1 * val2); 
                        break;
                case '/': s.push(val1 / val2); 
                        break;
            }
        }
    }
    return s.top();
}

int main() {
    string postfix;
    cout << "Enter postfix expression: ";
    cin >> postfix;
    
    cout << "Result: " << evaluate(postfix) << endl;
    return 0;
}

