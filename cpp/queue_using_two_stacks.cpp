#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <stack>
using namespace std;

class Queue{
    private:
        stack<int> stack1;
        stack<int> stack2;
        
        void move(){
            if (stack2.empty()){
                while (!stack1.empty()){
                    stack2.push(stack1.top());
                    stack1.pop();
                }
            }
        }
/*
        void debug(){
            for (stack<int> dump = stack1; !dump.empty(); dump.pop()){
                cout << dump.top() << '\n';
            }
            cout << "(" << stack1.size() << " elements)\n";

            for (stack<int> dump = stack2; !dump.empty(); dump.pop()){
                cout << dump.top() << '\n';
            }
            cout << "(" << stack2.size() << " elements)\n";
        }
 */
    public:
        void enqueue(int item) {
            stack1.push(item);
        }
        
        int denqueue() {
            move();
            int result = stack2.top();
            stack2.pop();
            return result;
        }
        
        void printqueue(){
            move();
            cout << stack2.top() << endl;
        }
};

int main() {
    Queue *q = new Queue();
    int queries;
    int type, value;
    cin >> queries;
    for(int i=0; i<queries; i++){
        cin >> type;
        switch(type){
            case 1:
                cin >> value;
                q->enqueue(value);
                break;
            case 2:
                q->denqueue();
                break;
            case 3:
                q->printqueue();
                break;
        }
    }
    
    return 0;
}
