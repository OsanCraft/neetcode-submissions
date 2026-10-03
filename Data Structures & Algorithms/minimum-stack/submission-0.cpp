#include <stack>
using namespace std;

class MinStack {

private:
    stack<int> final;
    stack<int> min;

public:
    MinStack() {

        
    }
    
    void push(int val) {
        final.push(val);

        if(min.empty() || val <= min.top()){
            min.push(val);
        }        
    }
    
    void pop() {

        if(final.top() == min.top()){
            min.pop();
        }
        
        final.pop();
    }
    
    int top() {
        return final.top();
        
    }
    
    int getMin() {

        return min.top();

        
    }
};
