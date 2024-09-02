#include <string>
#include <stack>
#include <iostream>
using namespace std;

// NOTE: I decided to follow the hackerrank variable names!
// I of course can give better variable names myself in production...

class Editor{
    private:
        string s;
        stack<string> last_strings;

    public:
        void append(string w) {
            last_strings.push(s);
            //cout << "append " << s << " ";
            s.append(w);
            //cout << s << endl;
        }
        void deleteFromPos(unsigned int k) {
            //cout << "deleteFromPos " << k << " ";
            last_strings.push(s);
            s.erase(s.size()-k, string::npos);
            //cout << s << endl;
        }
        void print(unsigned int k) {
            cout << s[k] << endl;
        }
        void undo() {
            if(last_strings.empty()){
                cout << "Warning: no more operations to undo!" << endl;
            } else {
                s = last_strings.top();
                last_strings.pop();
            }
            //cout << s << endl;
        }
};

int main() {
    Editor *e = new Editor();
    int queries;
    cin >> queries;
    for(int i=0; i<queries; i++){
        int type;
        string w;
        unsigned int k;
        cin >> type;
        switch(type){
            case 1:
                cin >> w;
                e->append(w);
                break;
            case 2:
                cin >> k;
                e->deleteFromPos(k);
                break;
            case 3:
                cin >> k;
                e->print(k-1);
                break;
            case 4:
                e->undo();
                break;
            default:
                break;
        }
    }
    
    return 0;
}