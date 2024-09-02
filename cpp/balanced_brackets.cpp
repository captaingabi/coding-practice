#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'isBalanced' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

bool match(char first, char second){
    switch(first){
        case '{':
            if (second == '}') return true;
            else return false;
        break;
            case '(':
            if (second == ')') return true;
            else return false;
            break;
        case '[':
            if (second == ']') return true;
            else return false;
            break;
        default:
            return false;
            break;
    }
}

string isBalanced(string s) {
    stack<char> stack;
    for(char& c : s) {
        if(c == '\0' or c == '\n' or c == '\r') break;
        if (!stack.empty() && match(stack.top(), c)) {
            stack.pop();
        } else {
            stack.push(c);
        }
    }
/*
    for (std::stack<char> dump = stack; !dump.empty(); dump.pop()){
        cout << dump.top() << '\n';
    }
    cout << "(" << stack.size() << " elements)\n";
*/
    return stack.empty() ? "YES" : "NO";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string s;
        getline(cin, s);

        string result = isBalanced(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
